import os
import subprocess
import sys

from Maquina2.Presentation.MenuExame import MenuExame


class MenuInicial:
    def __init__(self, facade):
        self.facade = facade

    def printMenu(self):
        comunicacao = False
        while True:

            print("+----------------MENU INICIAL-------------+")
            print("+                                         +")
            print("+   1 - Consultar Exames não realizados   +")
            print("+                                         +")
            print("+   2 - Escolher Exame                    +")
            print("+                                         +")
            print("+   3 - Definir Ligação                   +")
            print("+                                         +")
            print("+   4 - Sair                              +")
            print("+                                         +")
            print("+   5 - Iniciar comunicação               +")
            print("+                                         +")
            print("+-----------------------------------------+")

            opcao = int(input())

            if opcao == 1:
                self.printExames()
                continue
            if opcao == 2:
                self.escolherExame()
                continue
            if opcao == 3:
                self.printMenuComunicacao()
                continue
            if opcao == 4:
                sys.exit()
            if opcao == 5 and not comunicacao:
                os.system("start \"Thread Exames\" py \"Business/ListaTrabalho_ExameThread.py\"")
                # command1 = subprocess.Popen(['py', 'Business/ListaTrabalho_ExameThread.py'])
                comunicacao = True
                continue
            else:
                print("Opção Inválida !")

    def printExames(self):
        exames = self.facade.getExamesNaoRealizados()

        for (exame) in exames:
            print(exame)

    def escolherExame(self):
        id = input("Identificador do Exame: ")
        if self.facade.exameRealizadoExiste(id):
            MenuExame(self.facade, id).printMenu()
        else:
            print("Exame indisponível para avaliação !")

    def printMenuComunicacao(self):
        if self.facade.comunicacaoExists():
            while True:
                print("+-------Comunicacao--------+")
                print("+                          +")
                print("+  Definições Actuais:     +")
                print("+      IP: " + self.facade.getIp())
                print("+      Porta: " + self.facade.getPorta())
                print("+                          +")
                print("+  1  -  Redefinir         +")
                print("+                          +")
                print("+  2  -  Sair              +")
                print("+                          +")
                print("+--------------------------+")

                opcao = int(input())

                if opcao == 1:
                    ip = input("IP: ")
                    porta = input("Porta: ")
                    self.facade.updateComunicacao(ip, porta)
                    continue
                if opcao == 2:
                    return
        else:
            print("Defina os dados da comunicacao: ")
            ip = input("IP: ")
            porta = input("Porta: ")
            self.facade.insertComunicacao(ip, porta)
