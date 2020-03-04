from Maquina2.Persistence.SQLConnection import SQLConnection


class ComunicacaoDAO:
    def __init__(self):
        self.connector = SQLConnection().get_con()

    def insertComunicacao(self, ip, porta):
        cursor = self.connector.cursor(buffered=True)
        insert = ("INSERT INTO Comunicacao "
                  "(idCommunication, ip, porta)"
                  "VALUES (%(id)s, %(ip)s, %(porta)s )")
        dados = {
            'id': 1,
            'ip': ip,
            'porta': porta,
        }
        cursor.execute(insert, dados)
        self.connector.commit()
        cursor.close()

    def updateComunicacao(self, ip, porta):
        cursor = self.connector.cursor(buffered=True)
        update = ("UPDATE Comunicacao SET ip = '"+ ip +"', porta = '"+porta +"' WHERE idComunicacao = 1")
        cursor.execute(update)
        self.connector.commit()
        cursor.close()