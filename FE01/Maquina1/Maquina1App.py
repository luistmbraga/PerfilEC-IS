import os
import subprocess

from Maquina1.Business.Facade import Facade
from Maquina1.Presentation.MenuInicial import MenuInicial


if __name__ == "__main__":
    os.system("start \"Maquina1 Server\" py \"Business/Server.py\"")
    facade = Facade()
    ui = MenuInicial(facade)
    ui.printMenu()
