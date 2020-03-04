from Maquina2.Persistence.SQLConnection import SQLConnection


class ComunicacaoDAO:
    def __init__(self):
        self.connector = SQLConnection().get_con()

    def insertComunicacao(self, ip, porta):
        cursor = self.connector.cursor(buffered=True)
        insert = ("INSERT INTO Comunicacao "
                  "(idComunicacao, ip, porta) "
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

    def comunicacaoExists(self):
        query = ("SELECT ip FROM comunicacao WHERE idComunicacao = 1")
        cursor = self.connector.cursor()
        cursor.execute(query)
        r = cursor.fetchone() is not None
        cursor.close()
        return r

    def getIp(self):
        cursor = self.connector.cursor(buffered=True)
        query = "SELECT ip FROM comunicacao WHERE idComunicacao = 1"
        cursor.execute(query)
        comunicacao = cursor.fetchone()
        ip = str(comunicacao[0])
        cursor.close()
        return ip

    def getPorta(self):
        cursor = self.connector.cursor(buffered=True)
        query = "SELECT porta FROM comunicacao WHERE idComunicacao = 1"
        cursor.execute(query)
        comunicacao = cursor.fetchone()
        porta = str(comunicacao[0])
        cursor.close()
        return porta
