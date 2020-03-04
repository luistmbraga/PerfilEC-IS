import socket  # Import socket module
from hl7apy.parser import parse_message  # Message Parser
import mysql.connector
from dateutil import parser
from datetime import date, datetime, timedelta

s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345  # Reserve a port for your service.
s.bind((host, port))  # Bind to the port

s.listen(5)  # Now wait for client connection.
cnx = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              database='exames')
while True:
    c, addr = s.accept()  # Establish connection with client.
    print ('Got connection from', addr)
    line = ""
    ids = []
    while not (line.endswith("$")):
        line += c.recv(1024)
    print(line.replace('\r', '\n'))
    mensagens = line[:-1].split("$")
    for m in mensagens:
        message = parse_message(m)
        print (message.children)
        # Get Patient Info
        iddoente = message.ORM_O01_PATIENT.pid.pid_2.value
        numprocesso = message.ORM_O01_PATIENT.pid.pid_3.value
        nome = message.ORM_O01_PATIENT.pid.pid_5.value
        morada = message.ORM_O01_PATIENT.pid.pid_11.value
        telefone = message.ORM_O01_PATIENT.pid.pid_13.value
        # Get Message Content
        idpedido = message.ORM_O01_ORDER.ORC.orc_2.value
        estado = message.ORM_O01_ORDER.orc.orc_1.value
        mdata = message.ORM_O01_ORDER.ORC.orc_10.value
        observacoes = message.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_13.value
        idepisodio = message.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_4.value
        relatorio = message.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_12.value
        if estado == "CN":
            estado = "Canceled"
        if estado == "SH":
            estado = "Scheduled"
        # Insert/Update Patient Info
        cursor = cnx.cursor()
        insert = "INSERT INTO `Exames`.`Doente` (`idDoente`, `numProcesso`, `Nome`, `Morada`, `Telefone`) VALUES (%(idDoente)s,%(numProcesso)s,%(Nome)s,%(Morada)s,%(Telefone)s) ON DUPLICATE KEY UPDATE `numProcesso`= %(numProcesso)s, `Nome`= %(Nome)s, `Morada`=%(Morada)s , `Telefone`=%(Telefone)s "
        data = {
            'idDoente': iddoente,
            'numProcesso': numprocesso,
            'Nome': nome,
            'Morada': morada,
            'Telefone': telefone
        }
        cursor.execute(insert, data)
        cnx.commit()
        # Insert/Update Exam Info
        insert2 = "INSERT INTO `Exames`.`Pedido` (`idPedido`, `Estado`, `data`, `Observacoes`, `Doente_idDoente`, `idEpisodio`, `Relatorio`) VALUES ( %(idPedido)s , %(Estado)s , %(data)s, %(Observacoes)s, %(Doente_idDoente)s,%(idEpisodio)s, %(Relatorio)s) ON DUPLICATE KEY UPDATE  `Estado`=%(Estado)s, `data`=%(data)s, `Observacoes`=%(Observacoes)s, `Doente_idDoente`=%(Doente_idDoente)s, `idEpisodio`=%(idEpisodio)s, `Relatorio` =%(Relatorio)s"
        data2 = {
            'idPedido': int(idpedido),
            'Estado': estado,
            'data': parser.parse(mdata),
            'Observacoes': observacoes,
            'Doente_idDoente': iddoente,
            'idEpisodio': int(idepisodio),
            'Relatorio': relatorio
        }
        cursor.execute(insert2, data2)
        cnx.commit()
        ids.append(idpedido)
    c.send("ACK-" + ",".join(ids)+"$")
    c.close()  # Close the connection
