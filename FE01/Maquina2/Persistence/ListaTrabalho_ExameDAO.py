from Maquina2.Persistence.SQLConnection import SQLConnection


class ListaTrabalho_ExameDAO:
    def __init__(self):
        self.connector = SQLConnection().get_con()

    def insertNovoPedido(self, idExame):
        cursor = self.connector.cursor(buffered=True)
        insert = ("INSERT INTO ListaTrabalho_Exame "
                  "(Exames_idExames) "
                  "VALUES (%(idExame)s)")
        dados = {
            'idExame': idExame
        }
        cursor.execute(insert, dados)
        self.connector.commit()
        cursor.close()

    def getAll(self):
        query = "SELECT * FROM ListaTrabalho_Exame"
        cursor = self.connector.cursor()
        cursor.execute(query)
        return cursor

    def deletePedidoByID(self, id):
        cursor = self.connector.cursor(buffered=True)
        delete = ("DELETE FROM ListaTrabalho_Exame WHERE idListaTrabalho_Exame = " + str(id))
        cursor.execute(delete)
        self.connector.commit()
        cursor.close()
