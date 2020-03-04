from Maquina2.Persistence.SQLConnection import SQLConnection
from Maquina2.Business.Models.Consulta import Consulta


class ConsultaDAO:
    def __init__(self):
        self.connector = SQLConnection().get_con()

    def insertConsulta(self, Utente_idUtente, nomemedico, data):
        cursor = self.connector.cursor(buffered=True)
        insert = ("INSERT INTO Consulta "
                  "(Utente_idUtente, nomemedico, data)"
                  "VALUES (%(idUtente)s, %(nomemedico)s, %(data)s )")
        dados = {
            'idUtente': Utente_idUtente,
            'nomemedico': nomemedico,
            'data': data,
        }
        cursor.execute(insert, dados)
        self.connector.commit()
        cursor.close()

    def insertConsultaComId(self, idC, Utente_idUtente, nomemedico, data):
        cursor = self.connector.cursor(buffered=True)
        insert = ("INSERT INTO Consulta "
                  "(idConsulta, Utente_idUtente, nomemedico, data)"
                  "VALUES (%(id)s, %(idUtente)s, %(nomemedico)s, %(data)s )")
        dados = {
            'id': idC,
            'idUtente': Utente_idUtente,
            'nomemedico': nomemedico,
            'data': data,
        }
        cursor.execute(insert, dados)
        self.connector.commit()
        cursor.close()

    def getConsultasUtente(self, idUtente):
        query = "SELECT * FROM Consulta WHERE Utente_idUtente = " + idUtente
        cursor = self.connector.cursor()
        cursor.execute(query)
        result = []
        for (idConsulta, Utente_idUtente, nomemedico, data) in cursor:
            result.append(Consulta(idConsulta, Utente_idUtente, nomemedico, data))
        cursor.close()
        return result

    def getConsultaByID(self, idConsulta):
        query = "SELECT * FROM Consulta WHERE idConsulta = " + idConsulta
        cursor = self.connector.cursor()
        cursor.execute(query)
        consulta = cursor.fetchone()
        r = Consulta(str(consulta[0]), str(consulta[1]), str(consulta[2]), str(consulta[3]))
        cursor.close()
        return r

    def consultaNotExists(self, idU, idC):
        query = ("SELECT c.idConsulta "
                 "FROM Consulta c, Utente u "
                 "WHERE c.idConsulta = "+idC+" AND u.idUtente = "+idU+" AND u.idUtente = c.Utente_idUtente")
        cursor = self.connector.cursor()
        cursor.execute(query)
        r = cursor.fetchone() is None
        cursor.close()
        return r