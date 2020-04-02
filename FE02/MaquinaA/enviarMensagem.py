import socket
import time
import mysql.connector
from hl7apy.parser import parse_message

ss = socket.socket()
host = "localhost"
porta = 3001
ss.bind((host, 3002))

wait = 10

while True:
    con = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='fe02MaquinaA')

    query = "SELECT idMensagem, mensagemTxt FROM Mensagem WHERE vista = FALSE"
    cursor = con.cursor(buffered=True)
    cursor.execute(query)

    for (idMensagem, mensagemTxt) in cursor:

        msg = parse_message(mensagemTxt)

        start = time.time()

        cs = socket.socket()
        cs.connect((host, porta))
        cs.send(msg.value.encode('utf-8'))
        cs.close()

        ss.listen(1)
        conn, addr = ss.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)

        end = time.time()

        print("Resposta recebida")

        cursor2 = con.cursor(buffered=True)
        update = ("UPDATE Mensagem "
                  "SET vista = TRUE, roundTripTime = "+ str(end-start) +
                  " WHERE idMensagem = " + str(idMensagem))
        cursor2.execute(update)
        con.commit()
        cursor2.close()

    cursor.close()
    time.sleep(10)