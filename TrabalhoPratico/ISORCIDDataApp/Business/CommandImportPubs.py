import os

from Business.Command import Command


class CommandImportPubs(Command):

    def importPubs(self, filename):
        command = "mongoimport --db ISORCID --collection publicacoes --file {} --jsonArray"
        os.system(command.format(filename))

    def executeWithString(self, filename) -> None:
        self.importPubs(str(filename))

    def execute(self) -> None:
        print("Nada")
