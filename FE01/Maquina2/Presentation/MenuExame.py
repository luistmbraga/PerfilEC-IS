class MenuExame:
    def __init__(self, facade, exameId):
        self.facade = facade
        self.idExame = exameId

    def printMenu(self):
        while True:
            print("+----------EXAME - " + self.idExame + "---------------+")
            print(self.facade.getExame(self.idExame))
            print("+                                 +")
            print("+      1  -  Finalizar Exame      +")
            print("+                                 +")
            print("+      2  -  Escrever relatório   +")
            print("+                                 +")
            print("+      3  -  Sair                 +")
            print("+                                 +")
            print("+---------------------------------+")

            opcao = int(input())

            if opcao == 1:
                str = self.facade.finalizarExame(self.idExame)
                print(str)
                continue
            if opcao == 2:
                relatorio = input("Relatório: ")
                str = self.facade.escreverRelatorio(self.idExame, relatorio)
                print(str)
                return
            if opcao == 3:
                return
            else:
                print("Opcção Inválida !")