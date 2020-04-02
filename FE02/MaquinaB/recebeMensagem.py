import socket
from hl7apy.parser import parse_message
import mysql.connector
from hl7apy import core
from hl7apy.consts import VALIDATION_LEVEL

ss = socket.socket()
host = "localhost"
port = 3001
ss.bind((host, port))
while True:
    con = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='fe02MaquinaB')
    ss.listen(1)
    conn, addr = ss.accept()
    with conn:
        print('Connected by', addr)
        str = ""
        while True:
            data = []
            data = conn.recv(1024)
            str = str + data.decode('utf-8')
            if(len(data) == 0): break

        hl7 = parse_message(str)

        cursor = con.cursor(buffered=True)
        insert = ("INSERT INTO Inbox "
                  "(mensagemTxt) "
                  "VALUES (%(mensagem)s)")
        dados = {'mensagem': hl7.value}
        cursor.execute(insert, dados)
        con.commit()
        cursor.close()

        cs = socket.socket()
        cs.connect((host, 3002))
        ack = core.Message("ACK", validation_level=VALIDATION_LEVEL.STRICT)
        ack.msh.msh_9 = "ACK"
        ack.msh.msh_10 = "1"
        ack.msh.msh_11 = "1"
        ack.add_segment("MSA")
        ack.msa.msa_1 = "AA"
        ack.msa.msa_2 = "1"
        cs.send(ack.value.encode('utf-8'))
        cs.close()

