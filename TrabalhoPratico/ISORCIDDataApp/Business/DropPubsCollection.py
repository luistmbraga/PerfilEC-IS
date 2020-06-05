from Business.Command import Command
from Persistence.dbConnection import pubscol


class DropPubsCollection(Command):

    def dropPubsCollection(self):
        pubscol.drop()

    def execute(self) -> None:
        self.dropPubsCollection()
