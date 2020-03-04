# -*- coding: utf-8 -*-

import mysql.connector
from datetime import date, datetime, timedelta
from hl7apy import core
from hl7apy.consts import VALIDATION_LEVEL
import socket
import sched, time
from random import randint

sch = sched.scheduler(time.time, time.sleep)


cnx = mysql.connector.connect(user='python', password='Python1!',
                              host='127.0.0.1',
                              database='exames')
numMensagens = 0
mensagensMinuto = 0


def pedidosclient(sc):
    print("PedidosClient")
    mensagems = []
    numMessage = randint(1, 2500)
    global numMensagens,mensagensMinuto
    for x in range(0, numMessage):
        # Create Message
        hl7 = core.Message("ORM_O01", validation_level=VALIDATION_LEVEL.STRICT)

        # Message Header
        hl7.msh.msh_3 = "PedidosClient"
        hl7.msh.msh_4 = "PedidosClient"
        hl7.msh.msh_5 = "ExamesServer"
        hl7.msh.msh_6 = "ExamesServer"
        hl7.msh.msh_9 = "ORM^O01^ORM_O01"
        hl7.msh.msh_10 = str(randint(1, 200))
        hl7.msh.msh_11 = "P"

        # PID
        # https://corepointhealth.com/resource-center/hl7-resources/hl7-pid-segment

        hl7.add_group("ORM_O01_PATIENT")
        hl7.ORM_O01_PATIENT.pid.pid_2 = str(randint(1, 2500))  # id
        hl7.ORM_O01_PATIENT.pid.pid_3 = str(randint(1, 2500))  # processo
        hl7.ORM_O01_PATIENT.pid.pid_5 = str("Benchmark")
        hl7.ORM_O01_PATIENT.pid.pid_11 = str("Computer")
        hl7.ORM_O01_PATIENT.pid.pid_13 = str("253123456")

        # PV1
        # Não vai ter conter info (mas é necessária para uma mensagem válida)
        # https://corepointhealth.com/resource-center/hl7-resources/hl7-pv1-patient-visit-information-segment

        hl7.ORM_O01_PATIENT.add_group("ORM_O01_PATIENT_VISIT")
        hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.add_segment("PV1")
        hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_1 = "1"
        hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_2 = "1"

        # ORC
        # https://corepointhealth.com/resource-center/hl7-resources/hl7-obr-segment
        hl7.ORM_O01_ORDER.orc.orc_1 = "SH"
        hl7.ORM_O01_ORDER.ORC.orc_2 = str(randint(1, 2500))  # idpedido
        hl7.ORM_O01_ORDER.ORC.orc_10 = "2017-10-10"

        # OBR
        # https://corepointhealth.com/resource-center/hl7-resources/hl7-obr-segment

        hl7.ORM_O01_ORDER.add_group("ORM_O01_ORDER_DETAIL")
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.add_segment("ORM_O01_ORDER_CHOICE")
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("OBR")
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_13 = "Observações"
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_12 = "Relatorio"
        hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_4 = str(randint(1, 2500))  # idepisodio

        mensagems.append(hl7.value)
        mensagensMinuto = mensagensMinuto + 1
        numMensagens = numMensagens + 1
        print ("Message created")

    a = "$".join(mensagems)
    a += "$"
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.connect((host, port))
    s.send(a)
    s.close
    line = ""
    while not (line.endswith("$")):
        line += s.recv(1024)
    print(line[:-1])
    sch.enter(1, 1, pedidosclient, (sc,))


def pedidosclient2(sc):
    global numMensagens,mensagensMinuto
    print("Total mensagens envidadas=" + str(numMensagens))
    print("Mensagens envidadas este minuto=" + str(mensagensMinuto))
    mensagensMinuto = 0
    sch.enter(60, 1, pedidosclient2, (sch,))


sch.enter(0, 1, pedidosclient, (sch,))
sch.enter(0, 1, pedidosclient2, (sch,))

sch.run()
