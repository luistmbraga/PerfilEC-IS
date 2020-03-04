from Maquina1.Presentation.MenuExame import MenuExame
from Maquina1.Presentation.MenuRegistarExame import MenuRegistarExame


class MenuConsulta:
    def __init__(self, facade, utenteId, consultaId):
        self.facade = facade
        self.idUtente = utenteId
        self.idConsulta = consultaId

    def printMenu(self):
        while True:
            print("+-UTENTE - "+self.idUtente+" -> CONSULTA - "+self.idConsulta+"----+")
            print(self.facade.getConsulta(self.idConsulta))
            print("+    1  -  Registar Exame     +")
            print("+                             +")
            print("+    2  -  Consultar Exames   +")
            print("+                             +")
            print("+    3  -  Escolher Exame     +")
            print("+                             +")
            print("+    4  -  Sair               +")
            print("+                             +")
            print("+-----------------------------+")

            opcao = int(input())

            if opcao == 1:
                MenuRegistarExame(self.facade, self.idUtente, self.idConsulta).printMenu()
                continue
            if opcao == 2:
                self.printExames()
                continue
            if opcao == 3:
                self.escolherExame()
                continue
            if opcao == 4:
                return
            else:
                print("Opcção Inválida !")

    def printExames(self):
        exames = self.facade.getExames(self.idConsulta)

        for (exame) in exames:
            print(exame)

    def escolherExame(self):
        id = input("Identificador do Exame: ")
        if self.facade.exameNotExists(self.idConsulta, id):
            print("Exame não existe !")
        else:
            MenuExame(self.facade, self.idUtente, self.idConsulta, id).printMenu()