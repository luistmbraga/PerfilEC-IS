import os
import subprocess

from Maquina2.Business.Facade import Facade
from Maquina2.Presentation.MenuInicial import MenuInicial


if __name__ == "__main__":
    os.system("start \"Maquina2 Server\" py \"Business/Server.py\"")
    facade = Facade()
    ui = MenuInicial(facade)
    ui.printMenu()
