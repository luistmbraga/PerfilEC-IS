import os
import os.path
from os import path

from Business.Command import Command


class CommandExportUser(Command):

    def __init__(self):
        self.dir = "../ExportDir/"
        self.filename = "(0)utilizadores.json"

    def export(self):
        name = self.filename
        count = 1
        while (path.exists(self.dir + name)):
            name = "(" + str(count) + ")" + name[3:]
            count += 1

        command = "mongoexport --collection=utilizadores --db=ISORCID --out={} --jsonArray --pretty"
        os.system(command.format(self.dir + name))

    def execute(self) -> None:
        self.export()
