from Maquina1.Presentation.MenuConsulta import MenuConsulta
from Maquina1.Presentation.MenuRegistarConsulta import MenuRegistarConsulta


class MenuUtente:
    def __init__(self, facade, utenteId):
        self.facade = facade
        self.idUtente = utenteId

    def printMenu(self):
        while True:
            print("+-------------UTENTE - "+ self.idUtente +"---------------+")
            print(self.facade.getUtente(self.idUtente))
            print("+      1  -  Registar Consulta        +")
            print("+                                     +")
            print("+      2  -  Consultar Consultas      +")
            print("+                                     +")
            print("+      3  -  Escolher Consulta        +")
            print("+                                     +")
            print("+      4  -  Sair                     +")
            print("+                                     +")
            print("+-------------------------------------+")

            opcao = int(input())

            if opcao == 1:
                MenuRegistarConsulta(self.facade, self.idUtente).printMenu()
                continue
            if opcao == 2:
                self.printConsultas()
                continue
            if opcao == 3:
                self.escolherConsulta()
                continue
            if opcao == 4:
                return
            else:
                print("Opcção Inválida !")

    def printConsultas(self):
        consultas = self.facade.getConsultas(self.idUtente)

        for(consulta) in consultas:
            print(consulta)

    def escolherConsulta(self):
        id = input("Identificador da Consulta: ")
        if self.facade.consultaNotExists(self.idUtente, id):
            print("Consulta não existe !")
        else:
            MenuConsulta(self.facade, self.idUtente, id).printMenu()