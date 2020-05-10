from Presentation.ProcurarNovasPubs import ProcurarNovasPubs


class MenuInicial:

    def printMenu(self):

        while True:

            print("++==============MENU INICIAL============++")
            print("++                                      ++")
            print("++   1 - Procurar novas publicações     ++")
            print("++                                      ++")
            print("++   2 - Atualizar Publicações          ++")
            print("++                                      ++")
            print("++   3 - Atualizar cotações             ++")
            print("++                                      ++")
            print("++   4 - Sair                           ++")
            print("++                                      ++")
            print("++======================================++")

            try:
                opcao = int(input())

                if opcao == 1:
                    ProcurarNovasPubs().printMenu()
                    continue
                if opcao == 2:

                    continue
                if opcao == 3:

                    continue
                if opcao == 4:
                    break
                else:
                    print("Opção Inválida !")
            except:
                print("Opção não numérica")