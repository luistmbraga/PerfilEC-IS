from Maquina2.Persistence.SQLConnection import SQLConnection
from Maquina2.Business.Models.Exame import Exame


class ExameDAO:
    def __init__(self):
        self.connector = SQLConnection().get_con()

    def insertExame(self, idExame, Consulta_idConsulta, estado, relatorio, informacaoClinicaExtra, exameCodigo):
        cursor = self.connector.cursor(buffered=True)
        insert = ("INSERT INTO Exame "
                  "(idExame, Consulta_idConsulta, estado, relatorio, informacaoClinicaExtra, codigoExame)"
                  "VALUES (%(idExame)s, %(idConsulta)s, %(estado)s, %(estado)s, %(relatorio)s, %(infoClinica)s, %(exameCodigo)s)")
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

    def insertExameSemId(self, Consulta_idConsulta, estado, relatorio, informacaoClinicaExtra, exameCodigo):
        cursor = self.connector.cursor(buffered=True)
        insert = ("INSERT INTO Exame "
                  "(Consulta_idConsulta, estado, relatorio, informacaoClinicaExtra, codigoExame)"
                  "VALUES (%(idConsulta)s, %(estado)s, %(relatorio)s, %(infoClinica)s, %(exameCodigo)s)")
        dados = {
            'idConsulta': Consulta_idConsulta,
            'estado': estado,
            'relatorio': relatorio,
            'infoClinica': informacaoClinicaExtra,
            'exameCodigo': exameCodigo
        }
        cursor.execute(insert, dados)
        self.connector.commit()
        lastrow = cursor.lastrowid
        cursor.close()
        return lastrow

    def updateRelatorio(self, idExame, relatorio):
        cursor = self.connector.cursor(buffered=True)
        update = ("UPDATE Exame "
                  "SET relatorio = '" + relatorio + "' "
                  "WHERE idExame = " + idExame + "")
        cursor.execute(update)
        self.connector.commit()
        cursor.close()

    def updateEstadoExame(self, idExame, estado):
        cursor = self.connector.cursor(buffered=True)
        update = ("UPDATE Exame "
                  "SET estado = '" + estado + "' "
                  "WHERE idExame = " + idExame + "")
        cursor.execute(update)
        self.connector.commit()
        cursor.close()

    def getExamesNaoRealizados(self):
        query = "SELECT * FROM Exame WHERE estado = 'NW' OR (estado = 'CM' AND relatorio = 'NULL')"
        cursor = self.connector.cursor()
        cursor.execute(query)
        result = []
        for (idExame, Consulta_idConsulta, estado, relatorio, informacaoClinicaExtra, exameCodigo) in cursor:
            result.append(Exame(idExame, Consulta_idConsulta, estado, relatorio, informacaoClinicaExtra, exameCodigo))
        cursor.close()
        return result

    def getExamesConsulta(self, idConsulta):
        query = "SELECT * FROM Exame WHERE Consulta_idConsulta = " + idConsulta
        cursor = self.connector.cursor()
        cursor.execute(query)
        result = []
        i = 0
        for (idExame, Consulta_idConsulta, estado, relatorio, informacaoClinicaExtra, exameCodigo) in cursor:
            result[i] = Exame(idExame, Consulta_idConsulta, estado, relatorio, informacaoClinicaExtra, exameCodigo)
            i += 1
        cursor.close()
        return result

    def getExameByID(self, idExame):
        query = "SELECT * FROM Exame WHERE idExame = " + str(idExame)
        cursor = self.connector.cursor()
        cursor.execute(query)
        consulta = cursor.fetchone()
        r = Exame(str(consulta[0]), str(consulta[1]), str(consulta[2]), str(consulta[3]), str(consulta[4]),
                  str(consulta[5]))
        cursor.close()
        return r

    def exameNaoRealizadoExiste(self, idE):
        query = ("SELECT estado, relatorio "
                 "FROM Exame "
                 "WHERE idExame = " + str(idE))
        cursor = self.connector.cursor()
        cursor.execute(query)
        dados = cursor.fetchone()
        r = ((dados is not None) and (str(dados[0]) == "NW" or (str(dados[0]) == "CM") and str(dados[1]) == "NULL"))
        cursor.close()
        return r
