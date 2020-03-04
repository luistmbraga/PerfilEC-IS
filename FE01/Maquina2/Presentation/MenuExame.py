class MenuExame:
    def __init__(self, facade, exameId):
        self.facade = facade
        self.idExame = exameId

    def printMenu(self):
        while True:
            print("+----------EXAME - " + self.idExame + "---------------+")
            print(self.facade.getExame(self.idExame))
            print("+      1  -  Escrever relatório   +")
            print("+                                 +")
            print("+      2  -  Sair                 +")
            print("+                                 +")
            print("+---------------------------------+")

            opcao = int(input())

            if opcao == 1:
                relatorio = input("Relatório: ")
                self.facade.escreverRelatorio(self.idExame, relatorio)
                print("Relatório efectuado !")
                return
            if opcao == 2:
                return
            else:
                print("Opcção Inválida !")