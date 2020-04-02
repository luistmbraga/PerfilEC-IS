import strgen
import random
import time
import mysql.connector

while True:

    con = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='fe02MaquinaA')
    numMensagens = int(input("Escreva o número de mensagens a gerar: "))
    n = numMensagens
    start = time.time()
    while numMensagens > 0:

        num250 = random.randrange(1, 250)
        num705 = random.randrange(1, 705)
        num300 = random.randrange(1, 300)
        num99999 = random.randrange(1, 99999)

        str250 = strgen.StringGenerator("[\d\w]{"+ str(num250) +"}").render()
        str705 = strgen.StringGenerator("[\d\w]{" + str(num705) + "}").render()
        str300 = strgen.StringGenerator("[\d\w]{" + str(num300) + "}").render()
        str99999 = strgen.StringGenerator("[\d\w]{" + str(num99999) + "}").render()

        hl7 = '\r'.join(("MSH|^~\&|Maquina1App|IS Hospital|Maquina2App|IS Exam Center|20200331191037||ORM^O01|32|P|2.5",
                         "PID||1|"+str250+"||"+str250+"|||M|||"+str250+"||"+str250+"|"+str250+"||"+str705+"|||123456789|||||||tuga||tuga",
                         "PV1|1||||||"+str250+"|||||||||||||||||||||||||||||||||||||20200310",
                         "ORC|NW||||",
                         "OBR||14||"+str705+"||||||||"+ str300,
                         "RQD",
                         "RQ1",
                         "RXO",
                         "ODS|||",
                         "ODT|",
                         "OBX|||observation identifier||"+str99999+"||||||T"))

        cursor = con.cursor(buffered=True)
        insert = ("INSERT INTO Mensagem "
                  "(mensagemTxt, vista) "
                  "VALUES (%(mensagem)s, FALSE)")
        dados = {'mensagem': hl7}
        cursor.execute(insert, dados)
        con.commit()
        cursor.close()

        numMensagens-=1

    end = time.time()

    cursor = con.cursor(buffered=True)
    insert = ("INSERT INTO Batch "
              "(numMensagens, tempoGeracao) "
              "VALUES (%(num)s, %(tempo)s)")
    dados = {
        'num': n,
        'tempo': end - start
    }
    cursor.execute(insert, dados)
    con.commit()
    cursor.close()