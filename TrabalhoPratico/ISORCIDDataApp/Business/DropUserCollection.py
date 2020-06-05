from Business.Command import Command
from Persistence.dbConnection import userscol


class DropUserCollection(Command):

    def dropUserCollection(self):
        userscol.drop()

    def execute(self) -> None:
        self.dropUserCollection()
