# -*- coding: utf-8 -*-

import mysql.connector
from datetime import date, datetime, timedelta
from hl7apy import core
from hl7apy.consts import VALIDATION_LEVEL
import socket
import sched, time

sch = sched.scheduler(time.time, time.sleep)

cnx = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              database='exames')


def examesclient(sc):
    print("Exames")
    query = "SELECT * FROM WorkList"
    cursor = cnx.cursor(buffered=True)
    cursor.execute(query)
    messages = []
    for (
            idWorkList, editTime, Pedido_idPedido, Estado, data, Obervacoes, Doente_idDoente, idEpisodio,
            Relatorio) in cursor:
        cursor2 = cnx.cursor(buffered=True)
        queryPatient = ("SELECT * FROM Doente WHERE idDoente =" + str(Doente_idDoente))
        cursor2.execute(queryPatient)
        patient = cursor2.fetchone()
        # Create Message
        hl7 = core.Message("ORM_O01", validation_level=VALIDATION_LEVEL.STRICT)

        # Message Header
        hl7.msh.msh_3 = "PedidosClient"
        hl7.msh.msh_4 = "PedidosClient"
        hl7.msh.msh_5 = "ExamesServer"
        hl7.msh.msh_6 = "ExamesServer"
        hl7.msh.msh_9 = "ORM^O01^ORM_O01"
        hl7.msh.msh_10 = str(idWorkList)
        hl7.msh.msh_11 = "P"

        # PID
        # https://corepointhealth.com/resource-center/hl7-resources/hl7-pid-segment

        hl7.add_group("ORM_O01_PATIENT")
        hl7.ORM_O01_PATIENT.pid.pid_2 = str(Doente_idDoente)
        hl7.ORM_O01_PATIENT.pid.pid_3 = str(patient[1])
        hl7.ORM_O01_PATIENT.pid.pid_5 = str(patient[2])
        hl7.ORM_O01_PATIENT.pid.pid_11 = str(patient[3])
        hl7.ORM_O01_PATIENT.pid.pid_13 = str(patient[4])

        # PV1
        # Não vai ter conter info (mas é necessária para uma mensagem válida)
        # https://corepointhealth.com/resource-center/hl7-resources/hl7-pv1-patient-visit-information-segment

        hl7.ORM_O01_PATIENT.add_group("ORM_O01_PATIENT_VISIT")
        hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.add_segment("PV1")
        hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_1 = "1"
        hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_2 = "1"

        # ORC
        # https://corepointhealth.com/resource-center/hl7-resources/hl7-obr-segment
        hl7.ORM_O01_ORDER.orc.orc_1 = "DN"
        hl7.ORM_O01_ORDER.ORC.orc_10 = data.strftime("%Y-%m-%d")
        hl7.ORM_O01_ORDER.ORC.orc_2 = str(Pedido_idPedido)

        # OBR
        # https://corepointhealth.com/resource-center/hl7-resources/hl7-obr-segment

        hl7.ORM_O01_ORDER.add_group("ORM_O01_ORDER_DETAIL")
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.add_segment("ORM_O01_ORDER_CHOICE")
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("OBR")
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_13 = Obervacoes
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_12 = Relatorio
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_4 = str(idEpisodio)
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("RQD")
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("RQ1")
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("RXO")
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("ODS")
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("ODT")

        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.ODS.ods_1 = ""
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.ODS.ods_3 = ""
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.ODT.odt_1 = ""

        assert hl7.validate() is True
        messages.append(hl7)
        print (hl7.value.replace('\r', '\n'))
        s = socket.socket()
        host = socket.gethostname()
        port = 54321
        s.connect((host, port))
        s.send(hl7.value)
        s.close
        cursor2 = cnx.cursor()
        delete = ("DELETE FROM WorkList WHERE idWorkList=" + str(idWorkList))
        cursor2.execute(delete)
        cnx.commit()
        cursor2.close()

    cursor.close()
    sch.enter(20, 1, examesclient, (sc,))


sch.enter(0, 1, examesclient, (sch,))
sch.run()
