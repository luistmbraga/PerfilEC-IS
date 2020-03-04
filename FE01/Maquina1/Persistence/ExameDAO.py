from Maquina1.Persistence.SQLConnection import SQLConnection
from Maquina1.Business.Models.Exame import Exame


class ExameDAO:
    def __init__(self):
        self.connector = SQLConnection().get_con()

    def insertExame(self, idExame, Consulta_idConsulta, estado, relatorio, informacaoClinicaExtra, exameCodigo):
        cursor = self.connector.cursor(buffered=True)
        insert = ("INSERT INTO Exame "
                  "(idExame, Consulta_idConsulta, estado, relatorio, informacaoClinicaExtra, exameCodigo)"
                  "VALUES (%(idExame)s, %(idConsulta)s, %(estado)s, %(relatorio)s, %(infoClinica)s, %(exameCodigo)s)")
        dados = {
            'idExame': idExame,
            'idConsulta': Consulta_idConsulta,
            'estado': estado,
            'relatorio': relatorio,
            'infoClinica': informacaoClinicaExtra,
            'exameCodigo': exameCodigo
        }
        cursor.execute(insert, dados)
        self.connector.commit()
        cursor.close()

    def updateEstadoExame(self, idExame, estado):
        cursor = self.connector.cursor(buffered=True)
        update = ("UPDATE Exame "
                  "SET estado = '"+estado+"' "
                  "WHERE idExame = "+idExame+"")
        cursor.execute(update)
        self.connector.commit()
        cursor.close()

    def getExamesConsulta(self, idConsulta):
        query = "SELECT * FROM Exame WHERE Consulta_idConsulta = " + idConsulta
        cursor = self.connector.cursor()
        cursor.execute(query)
        result = []
        for (idExame, Consulta_idConsulta, estado, relatorio, informacaoClinicaExtra, exameCodigo) in cursor:
            result.append(Exame(idExame, Consulta_idConsulta, estado, relatorio, informacaoClinicaExtra, exameCodigo))
        cursor.close()
        return result

    def getExameByID(self, idExame):
        query = "SELECT * FROM Exame WHERE idExame = " + idExame
        cursor = self.connector.cursor()
        cursor.execute(query)
        consulta = cursor.fetchone()
        r = Exame(str(consulta[0]), str(consulta[1]), str(consulta[2]), str(consulta[3]), str(consulta[4]), str(consulta[5]))
        cursor.close()
        return r

    def exameNotExists(self, idC, idE):
        query = ("SELECT idExame "
                 "FROM Exame e, Consulta c "
                 "WHERE e.idExame = "+idE+" AND c.idConsulta = "+idC+" AND c.idConsulta = e.Consulta_idConsulta")
        cursor = self.connector.cursor()
        cursor.execute(query)
        r = cursor.fetchone() is None
        cursor.close()
        return r
