from Maquina1.Persistence.SQLConnection import SQLConnection


class ListaTrabalho_PedidoDAO:
    def __init__(self):
        self.connector = SQLConnection().get_con()

    def insertNovoPedido(self, idConsulta, infoClinica, exame):
        cursor = self.connector.cursor(buffered=True)
        insert = ("INSERT INTO ListaTrabalho_Pedido "
                  "(Consulta_idConsulta, idExame, informacaoClinicaExtra, estado, exameCodigo) "
                  "VALUES (%(idConsulta)s, NULL, %(infoClinica)s, 'NW', %(exame)s)")
        dados = {
            'idConsulta': idConsulta,
            'infoClinica': infoClinica,
            'exame': exame
        }
        cursor.execute(insert, dados)
        self.connector.commit()
        cursor.close()

    def insertAlteracaoPedido(self, idConsulta, idExame, estado):
        cursor = self.connector.cursor(buffered=True)
        insert = ("INSERT INTO ListaTrabalho_Pedido "
                  "(Consulta_idConsulta, idExame, estado) "
                  "VALUES (%(idConsulta)s, %(idExame)s, %(estado)s)")
        dados = {
            'idConsulta': idConsulta,
            'idExame': idExame,
            'estado': estado,
        }
        cursor.execute(insert, dados)
        self.connector.commit()
        cursor.close()

    def getAll(self):
        cursor = self.connector.cursor(buffered=True)
        query = "SELECT * FROM ListaTrabalho_Pedido"
        cursor.execute(query)
        return cursor

    def deletePedidoByID(self, id):
        cursor = self.connector.cursor(buffered=True)
        delete = ("DELETE FROM ListaTrabalho_Pedido WHERE idListaTrabalho_Pedido = " + str(id))
        cursor.execute(delete)
        self.connector.commit()
        cursor.close()
