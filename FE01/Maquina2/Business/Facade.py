from Maquina2.Persistence.ComunicacaoDAO import ComunicacaoDAO
from Maquina2.Persistence.ConsultaDAO import ConsultaDAO
from Maquina2.Persistence.ExameDAO import ExameDAO
from Maquina2.Persistence.ListaTrabalho_ExameDAO import ListaTrabalho_ExameDAO
from Maquina2.Persistence.UtenteDAO import UtenteDAO


class Facade:
    def __init__(self):
        self.comunicacaoDAO = ComunicacaoDAO()
        self.consultaDAO = ConsultaDAO()
        self.exameDAO = ExameDAO()
        self.utenteDAO = UtenteDAO()
        self.listaTrabalhoDAO = ListaTrabalho_ExameDAO()

    def getExamesNaoRealizados(self):
        exames = self.exameDAO.getExamesNaoRealizados()
        exames_strings = []
        for (exame) in exames:
            exames_strings.append(exame.toString())
        self.__init__()
        return exames_strings

    def getExame(self, idExame):
        exame = self.exameDAO.getExameByID(idExame)
        self.__init__()
        return exame.toString()

    def exameNaoRealizadoExiste(self, idExame):
        r = self.exameDAO.exameNaoRealizadoExiste(idExame)
        self.__init__()
        return r

    def finalizarExame(self, idExame):
        exame = self.exameDAO.getExameByID(idExame)
        if exame.estado == "CM":
            str = "Exame já foi finalizado !"
        else:
            self.exameDAO.updateEstadoExame(idExame, "CM")
            self.listaTrabalhoDAO.insertNovoPedido(idExame)
            str = "Exame finalizado !"
        self.__init__()
        return str

    def escreverRelatorio(self, idExame, relatorio):
        exame = self.exameDAO.getExameByID(idExame)
        if exame.estado == "CM":
            str = "Relatório efectuado !"
            self.exameDAO.updateRelatorio(idExame, relatorio)
            self.listaTrabalhoDAO.insertNovoPedido(idExame)
        else:
            str = "Exame não finalizado !"
        self.__init__()
        return str

    #################### Comunicacao

    def insertComunicacao(self, ip, porta):
        self.comunicacaoDAO.insertComunicacao(ip, porta);
        self.__init__()

    def updateComunicacao(self, ip, porta):
        self.comunicacaoDAO.updateComunicacao(ip, porta)
        self.__init__()

    def comunicacaoExists(self):
        r = self.comunicacaoDAO.comunicacaoExists()
        self.__init__()
        return r

    def getIp(self):
        ip = self.comunicacaoDAO.getIp()
        self.__init__()
        return ip

    def getPorta(self):
        porta = self.comunicacaoDAO.getPorta()
        self.__init__()
        return porta
