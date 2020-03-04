import os
import subprocess

from Maquina1.Presentation.MenuRegistarUtente import MenuRegistarUtente
from Maquina1.Presentation.MenuUtente import MenuUtente
import sys


class MenuInicial:
    def __init__(self, facade):
        self.facade = facade

    def printMenu(self):
        comunicacao = False
        while True:

            print("+-------MENU INICIAL--------+")
            print("+                           +")
            print("+   1 - Registar Utente     +")
            print("+                           +")
            print("+   2 - Consultar Utentes   +")
            print("+                           +")
            print("+   3 - Escolher Utente     +")
            print("+                           +")
            print("+   4 - Definir Ligação     +")
            print("+                           +")
            print("+   5 - Sair                +")
            print("+                           +")
            print("+   6 - Iniciar comunicação +")
            print("+                           +")
            print("+---------------------------+")

            opcao = int(input())

            if opcao == 1:
                MenuRegistarUtente(self.facade).printMenu()
                continue
            if opcao == 2:
                self.printUtentes()
                continue
            if opcao == 3:
                self.escolherUtente()
                continue
            if opcao == 4:
                self.printMenuComunicacao()
                continue
            if opcao == 5:
                sys.exit()
            if opcao == 6 and not comunicacao:
                os.system("start \"Thread Pedidos\" py \"Business/ListaTrabalho_PedidoThread.py\"")
                # command1 = subprocess.Popen(['py', 'Business/ListaTrabalho_PedidoThread.py'])
                comunicacao = True
                continue
            else:
                print("Opção Inválida !")

    def printUtentes(self):
        utentes = self.facade.getUtentes()

        for (utente) in utentes:
            print(utente)

    def escolherUtente(self):
        id = input("Identificador do Utente: ")
        if self.facade.utenteNotExists(id):
            print("Utente não existe !")
        else:
            MenuUtente(self.facade, id).printMenu()

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
