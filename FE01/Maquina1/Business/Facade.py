from datetime import date

from Maquina1.Persistence.ComunicacaoDAO import ComunicacaoDAO
from Maquina1.Persistence.ConsultaDAO import ConsultaDAO
from Maquina1.Persistence.ExameDAO import ExameDAO
from Maquina1.Persistence.UtenteDAO import UtenteDAO
from Maquina1.Persistence.ListaTrabalho_PedidoDAO import ListaTrabalho_PedidoDAO


class Facade:
    def __init__(self):
        self.comunicacaoDAO = ComunicacaoDAO()
        self.consultaDAO = ConsultaDAO()
        self.exameDAO = ExameDAO()
        self.utenteDAO = UtenteDAO()
        self.listaTrabalhoDAO = ListaTrabalho_PedidoDAO()

    ################### Utente

    def addUtente(self, patientName, adminisSex, patientAddress, phNumberHome, phNumberWork, mariStatus, ssnNumber,
                  citizenship, nationality):
        self.utenteDAO.insertUtente(patientName, adminisSex, patientAddress, phNumberHome, phNumberWork, mariStatus,
                                    ssnNumber,
                                    citizenship, nationality)
        self.__init__()

    def getUtentes(self):
        utentes = self.utenteDAO.getAllUtentes()
        utentes_strings = []
        for (utente) in utentes:
            utentes_strings.append(utente.toString())
        self.__init__()
        return utentes_strings

    def getUtente(self, idUtente):
        utente = self.utenteDAO.getUtenteByID(idUtente)
        self.__init__()
        return utente.toString()

    def getConsultas(self, idUtente):
        consultas = self.consultaDAO.getConsultasUtente(idUtente)
        consultas_strings = []
        for (consulta) in consultas:
            consultas_strings.append(consulta.toString())
        self.__init__()
        return consultas_strings

    def utenteNotExists(self, idUtente):
        r = self.utenteDAO.utenteNotExists(idUtente)
        self.__init__()
        return r

    ################ Consulta

    def addConsulta(self, Utente_idUtente, nomemedico):
        self.consultaDAO.insertConsulta(Utente_idUtente, nomemedico, date.today())
        self.__init__()

    def getConsulta(self, idConsulta):
        consulta = self.consultaDAO.getConsultaByID(idConsulta)
        self.__init__()
        return consulta.toString()

    def getExames(self, idConsulta):
        exames = self.exameDAO.getExamesConsulta(idConsulta)
        exames_strings = []
        for (exame) in exames:
            exames_strings.append(exame.toString())
        self.__init__()
        return exames_strings

    def consultaNotExists(self, idUtente, idConsulta):
        r = self.consultaDAO.consultaNotExists(idUtente, idConsulta)
        self.__init__()
        return r

    ################# Exames

    def addNovoPedido(self, Consulta_idConsulta, infoClinica, exameCodigo):
        self.listaTrabalhoDAO.insertNovoPedido(Consulta_idConsulta, infoClinica, exameCodigo)
        self.__init__()

    def getExame(self, idExame):
        exame = self.exameDAO.getExameByID(idExame)
        self.__init__()
        return exame.toString()

    def exameNotExists(self, idC, idE):
        r = self.exameDAO.exameNotExists(idC, idE)
        self.__init__()
        return r

    def cancelarExame(self, idConsulta, idExame):
        exame = self.exameDAO.getExameByID(idExame)
        if exame.estado == "OK":
            str = "Exame já foi realizado !"
        if exame.estado == "CA":
            str = "Exame já foi cancelado !"
        else:
            self.listaTrabalhoDAO.insertAlteracaoPedido(idConsulta, idExame, "CA")
            str = "Exame cancelado !"
        self.__init__()
        return str
