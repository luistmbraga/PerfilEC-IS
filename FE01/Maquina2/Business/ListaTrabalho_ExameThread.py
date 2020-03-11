import sched
import socket
import time

from Maquina2.Business.Models.ORM_MESSAGE import ORM_MESSAGE
from Maquina2.Business.Models.ORU_MESSAGE import ORU_MESSAGE
from Maquina2.Persistence.ComunicacaoDAO import ComunicacaoDAO
from Maquina2.Persistence.ConsultaDAO import ConsultaDAO
from Maquina2.Persistence.ExameDAO import ExameDAO
from Maquina2.Persistence.ListaTrabalho_ExameDAO import ListaTrabalho_ExameDAO
from Maquina2.Persistence.UtenteDAO import UtenteDAO


class ListaTrabalho_ExameThread:
    def __init__(self):
        self.listaTrabalhoDAO = ListaTrabalho_ExameDAO()
        self.consultaDAO = ConsultaDAO()
        self.utenteDAO = UtenteDAO()
        self.comunicacaoDAO = ComunicacaoDAO()
        self.exameDAO = ExameDAO()
        self.sch = sched.scheduler(time.time, time.sleep)
        self.time = 3
        self.cs = socket.socket()
        if self.comunicacaoDAO.comunicacaoExists():
            self.host = self.comunicacaoDAO.getIp()
            self.porta = int(self.comunicacaoDAO.getPorta())
        else:
            self.host = "localhost" # "172.26.125.57"
            self.porta = 3001

    def run(self):
        while True:
            self.__init__()

            print("A thread exames está a correr")
            cursor = self.listaTrabalhoDAO.getAll()
            for (idListaTrabalho_Exame, Exames_idExames) in cursor:
                exame = self.exameDAO.getExameByID(Exames_idExames)
                idConsulta = exame.idConsulta
                consulta = self.consultaDAO.getConsultaByID(idConsulta)
                idUtente = consulta.idUtente
                utente = self.utenteDAO.getUtenteByID(idUtente)

                if exame.relatorio == "NULL":
                    hl7 = self.criaORMmessage(exame, consulta, utente, idListaTrabalho_Exame, Exames_idExames)
                else:
                    hl7 = self.criaORUMessage(idListaTrabalho_Exame, exame)

                self.cs.connect((self.host, self.porta))

                self.cs.send(hl7.getValue().encode('utf-8'))

                self.cs.close()

                self.listaTrabalhoDAO.deletePedidoByID(idListaTrabalho_Exame)

                cursor.close()

            time.sleep(self.time)

    def criaORMmessage(self, exame, consulta, utente, idListaTrabalho_Exame, Exames_idExames):
        hl7 = ORM_MESSAGE()
        # set_MSH(self, sendingApp, sendingFacility, receivingApp, receivingFacility, messageControlId, processingId)
        hl7.set_MSH("Maquina1App", "IS Hospital", "Maquina2App", "IS Exam Center", str(idListaTrabalho_Exame),
                    "P")
        # set_PID(self, patientIdExternal, patientIdInternal, patientName, adminisSex, patientAddress, phNumberHome, phNumberWork, mariStatus, ssnNumber, citizenship, nationality):
        hl7.set_PID(utente.idUtente, utente.idUtente, utente.nome, utente.sexo, utente.morada, utente.telefoneCasa,
                    utente.telefoneTrabalho, utente.estadoCivil, utente.ssn, utente.cidadania,
                    utente.nacionalidade)
        # set_PV1(self, sequenceId, attendingDoctor, admitTime)
        hl7.set_PV1(consulta.idConsulta, consulta.nomeMedico, consulta.data.replace('-', ''))
        # set_ORC(self, orderControl)
        if exame.estado == "CM":
            hl7.set_ORC("SC", exame.estado)
        else:
            hl7.set_ORC(exame.estado, "")
        # set_OBR(self, idExame, exameCodigo, clinicalInfo)
        hl7.set_OBR(Exames_idExames, exame.exameCodigo, exame.informacaoClinica)
        # set_OBX(self, relatorio)
        hl7.set_OBX("NULL")

        hl7.validate()

        print(hl7.print())

        return hl7

    def criaORUMessage(self, idListaTrabalho_Exame, exame):
        hl7 = ORU_MESSAGE()

        hl7.set_MSH("Maquina1App", "IS Hospital", "Maquina2App", "IS Exam Center", str(idListaTrabalho_Exame),
                    "P")

        hl7.set_OBR(exame.idExame, exame.exameCodigo, exame.informacaoClinica)

        hl7.set_OBX(exame.relatorio)

        hl7.validate()

        print(hl7.print())

        return hl7

if __name__ == "__main__":
    worklist = ListaTrabalho_ExameThread()
    worklist.run()
