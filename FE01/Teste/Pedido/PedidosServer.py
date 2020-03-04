import socket  # Import socket module
from hl7apy.parser import parse_message  # Message Parser
import mysql.connector
from datetime import date, datetime, timedelta

s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 54321  # Reserve a port for your service.
s.bind((host, port))  # Bind to the port

s.listen(5)  # Now wait for client connection.
cnx = mysql.connector.connect(user='python', password='Python1!',
                              host='127.0.0.1',
                              database='pedidos')
while True:
    c, addr = s.accept()  # Establish connection with client.
    print ('Got connection from', addr)
    m = c.recv(1024)
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
    data = message.ORM_O01_ORDER.ORC.orc_10.value
    observacoes = message.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_13.value
    idepisodio = message.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_4.value
    relatorio = message.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_12.value
    # Insert/Update Patient Info
    cursor = cnx.cursor()
    insert = "INSERT INTO `pedidos`.`Doente` (`idDoente`, `numProcesso`, `Nome`, `Morada`, `Telefone`) VALUES (%(idDoente)s,%(numProcesso)s,%(Nome)s,%(Morada)s,%(Telefone)s) ON DUPLICATE KEY UPDATE `numProcesso`= %(numProcesso)s, `Nome`= %(Nome)s, `Morada`=%(Morada)s , `Telefone`=%(Telefone)s "
    data = {
        'idDoente': iddoente,
        'numProcesso': numprocesso,
        'Nome': nome,
        'Morada': morada,
        'Telefone': telefone
    }
    cursor.execute(insert, data)
    # Insert/Update Request Info
    update = ("UPDATE Pedido SET Estado=\"Complete\", Relatorio = \'" + str(relatorio) + "\'WHERE idPedido = " + str(idpedido))
    cursor.execute(update)
    cnx.commit()
    c.close()  # Close the connection
