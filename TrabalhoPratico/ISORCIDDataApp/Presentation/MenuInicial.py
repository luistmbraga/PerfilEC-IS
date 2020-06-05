from Business.Facade import Facade


class MenuInicial:

    def __init__(self):
        self.facade = Facade()

    def printMenu(self):

        while True:

            print("++==============MENU INICIAL============++")
            print("++                                      ++")
            print("++   1 - Procurar novas publicações     ++")
            print("++                                      ++")
            print("++   2 - Atualizar citações, issn e SJR ++")
            print("++                                      ++")
            print("++   3 - Apagar coleção de publicações  ++")
            print("++                                      ++")
            print("++   4 - Apagar coleção de utilizadores ++")
            print("++                                      ++")
            print("++   5 - Exportar Publicações           ++")
            print("++                                      ++")
            print("++   6 - Exportar Utilizadores          ++")
            print("++                                      ++")
            print("++   7 - Importar Publicações           ++")
            print("++                                      ++")
            print("++   8 - Importar Utilizadores          ++")
            print("++                                      ++")
            print("++   9 - Sair                           ++")
            print("++                                      ++")
            print("++======================================++")

            try:
                opcao = int(input())

                if opcao == 1:
                    self.facade.executePubSearcher()
                    continue
                if opcao == 2:
                    self.facade.executeAtualizaCitacoes()
                    continue
                if opcao == 3:
                    self.facade.executeDropPubs()
                    continue
                if opcao == 4:
                    self.facade.executeDropUser()
                    continue
                if opcao == 5:
                    self.facade.executeExportPubs()
                    continue
                if opcao == 6:
                    self.facade.executeExportUser()
                    continue
                if opcao == 7:
                    name = input("Nome do ficheiro para onde enviar: ")
                    self.facade.executeImportPubs(name)
                    continue
                if opcao == 8:
                    name = input("Nome do ficheiro para onde enviar: ")
                    self.facade.executeImportUser(name)
                    continue
                if opcao == 9:
                    break
                else:
                    print("Opção Inválida !")
            except:
                print("Opção não numérica")


if __name__ == '__main__':
    menu = MenuInicial()
    menu.printMenu()
