from Business.AtualizaCitacoes import AtualizaCitacoes
from Business.CommandExportPubs import CommandExportPubs
from Business.CommandExportUser import CommandExportUser
from Business.CommandImportPubs import CommandImportPubs
from Business.CommandImportUser import CommandImportUser
from Business.PubSearcher import PubSearcher
from Business.DropPubsCollection import DropPubsCollection
from Business.DropUserCollection import DropUserCollection


class Facade:

    def __init__(self):
        self.commandPubSearcher = PubSearcher()
        self.commandDropPubs = DropPubsCollection()
        self.commandDropUser = DropUserCollection()
        self.commandExportPubs = CommandExportPubs()
        self.commandImportPubs = CommandImportPubs()
        self.commandAtualizaCitacoes = AtualizaCitacoes()
        self.commandExportUser = CommandExportUser()
        self.commandImportUser = CommandImportUser()

    def executePubSearcher(self):
        self.commandPubSearcher.execute()

    def executeDropPubs(self):
        self.commandDropPubs.execute()

    def executeDropUser(self):
        self.commandDropUser.execute()

    def executeExportPubs(self):
        self.commandExportPubs.execute()

    def executeImportPubs(self, filename):
        self.commandImportPubs.executeWithString(filename)

    def executeAtualizaCitacoes(self):
        self.commandAtualizaCitacoes.execute()

    def executeExportUser(self):
        self.commandExportUser.execute()

    def executeImportUser(self, filename):
        self.commandImportUser.executeWithString(filename)
