class MenuExame:
    def __init__(self, facade, utenteId, consultaId, exameId):
        self.facade = facade
        self.idUtente = utenteId
        self.idConsulta = consultaId
        self.idExame = exameId

    def printMenu(self):
        while True:
            print("+-UTENTE - "+self.idUtente+" -> Consulta - "+self.idConsulta+" -> EXAME - " + self.idExame + "---------------+")
            print(self.facade.getExame(self.idExame))
            print("+      1  -  Cancelar Exame       +")
            print("+                                 +")
            print("+      2  -  Sair                 +")
            print("+                                 +")
            print("+---------------------------------+")

            opcao = int(input())

            if opcao == 1:
                result = self.facade.cancelarExame(self.idConsulta, self.idExame)
                print(result)
                return
            if opcao == 2:
                return
            else:
                print("Opcção Inválida !")