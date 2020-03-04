from Maquina1.Business.Facade import Facade


class MenuRegistarExame:
    def __init__(self, facade, utenteId, consultaId):
        self.facade = facade
        self.idUtente = utenteId
        self.idConsulta = consultaId

    def printMenu(self):
        print("+---------REGISTAR EXAME---------+")

        infoClinica = input("Informacao Clinica Extra: ")
        exameCodigo = input("Exame a requerer: ")

        self.facade.addNovoPedido(self.idConsulta, infoClinica, exameCodigo)

        print("Exame registado com sucesso !")

        return