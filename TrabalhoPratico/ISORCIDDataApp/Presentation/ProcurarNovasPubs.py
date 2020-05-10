import os

class ProcurarNovasPubs:

    def printMenu(self):

        while True:

            print("++==============Procurar Novas Publicações============++")
            print("++                                                    ++")
            print("++      Detalhes:                                     ++")
            print("++                                                    ++")
            print("++                                                    ++")
            print("++                                                    ++")
            print("++      1 - Procurar                                  ++")
            print("++                                                    ++")
            print("++      2 - Sair                                      ++")
            print("++                                                    ++")
            print("++====================================================++")


            try:
                opcao = int(input())

                if opcao == 1:
                    os.system("start \"Procurar Novas Publicações\" py \"../Business/pubSearcher.py\"")
                    continue
                if opcao == 2:
                    break
                else:
                    print("Opção Inválida !")
            except:
                print("Opção não numérica")