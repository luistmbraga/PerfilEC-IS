class MenuRegistarConsulta:
    def __init__(self, facade, utenteId):
        self.facade = facade
        self.idUtente = utenteId


    def printMenu(self):
        print("+---------REGISTAR CONSULTA---------+")

        nomemedico = input("Nome do Medico: ")

        self.facade.addConsulta(self.idUtente, nomemedico)

        print("Consulta registada com sucesso !")

        return