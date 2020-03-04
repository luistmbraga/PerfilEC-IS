from Maquina1.Persistence.SQLConnection import SQLConnection
from Maquina1.Business.Models.Utente import Utente


class UtenteDAO:
    def __init__(self):
        self.connector = SQLConnection().get_con()

    def insertUtente(self, patientName, adminisSex, patientAddress, phNumberHome, phNumberWork, mariStatus, ssnNumber,
                     citizenship, nationality):
        cursor = self.connector.cursor(buffered=True)
        insert = ("INSERT INTO Utente "
                  "(morada, telefoneCasa, telefoneTrabalho, nome, sexo, estadoCivil, ssn, nacionalidade, cidadania)"
                  "VALUES (%(morada)s, %(telefoneCasa)s, %(telefoneTrabalho)s, %(nome)s, %(sexo)s, %(estadoCivil)s, %(ssn)s, %(nacionalidade)s, %(cidadania)s )")
        dados = {
            'morada': patientAddress,
            'telefoneCasa': phNumberHome,
            'telefoneTrabalho': phNumberWork,
            'nome': patientName,
            'sexo': adminisSex,
            'estadoCivil': mariStatus,
            'ssn': ssnNumber,
            'nacionalidade': nationality,
            'cidadania': citizenship
        }
        cursor.execute(insert, dados)
        self.connector.commit()
        cursor.close()

    def getAllUtentes(self):
        query = "SELECT * FROM Utente"
        cursor = self.connector.cursor()
        cursor.execute(query)
        result = []
        for (idUtente, morada, telefoneCasa, telefoneTrabalho, nome, sexo, estadoCivil, ssn, nacionalidade,
             cidadania) in cursor:
            result.append(Utente(idUtente, morada, telefoneCasa, telefoneTrabalho, nome, sexo, estadoCivil, ssn,
                               nacionalidade, cidadania))
        cursor.close()
        return result

    def getUtenteByID(self, id):
        query = "SELECT * FROM Utente WHERE idUtente = " + id
        cursor = self.connector.cursor()
        cursor.execute(query)
        utente = cursor.fetchone()
        r = Utente(str(utente[0]), str(utente[1]), str(utente[2]), str(utente[3]), str(utente[4]),
                   str(utente[5]), str(utente[6]), str(utente[7]), str(utente[8]), str(utente[9]))
        cursor.close()
        return r

    def utenteNotExists(self, id):
        query = "SELECT idUtente FROM Utente WHERE idUtente = " + id
        cursor = self.connector.cursor()
        cursor.execute(query)
        r = cursor.fetchone() is None
        cursor.close()
        return r
