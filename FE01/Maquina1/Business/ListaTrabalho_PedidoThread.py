import socket

from Maquina1.Business.Models.ORM_MESSAGE import ORM_MESSAGE
from Maquina1.Persistence.ComunicacaoDAO import ComunicacaoDAO
from Maquina1.Persistence.ConsultaDAO import ConsultaDAO
from Maquina1.Persistence.ListaTrabalho_PedidoDAO import ListaTrabalho_PedidoDAO
import sched, time

from Maquina1.Persistence.UtenteDAO import UtenteDAO


class ListaTrabalho_PedidoThread:
    def __init__(self):
        self.listaTrabalhoDAO = ListaTrabalho_PedidoDAO()
        self.consultaDAO = ConsultaDAO()
        self.utenteDAO = UtenteDAO()
        self.comunicacaoDAO = ComunicacaoDAO()
        self.sch = sched.scheduler(time.time, time.sleep)
        self.time = 3
        self.cs = socket.socket()
        if self.comunicacaoDAO.comunicacaoExists():
            self.host = self.comunicacaoDAO.getIp()
            self.porta = int(self.comunicacaoDAO.getPorta())
        else:
            self.host = "localhost" # "172.26.125.57"
            self.porta = 3002

    def run(self):
        while True:
            self.__init__()

            print("A thread pedidos está a correr")
            cursor = self.listaTrabalhoDAO.getAll()
            for(idListaTrabalho_Pedido, Consulta_idConsulta, idExame, informacaoClinicaExtra, estado, exameCodigo) in cursor:
                consulta = self.consultaDAO.getConsultaByID(Consulta_idConsulta)
                idUtente = consulta.idUtente
                utente = self.utenteDAO.getUtenteByID(idUtente)

                hl7 = ORM_MESSAGE()
                # set_MSH(self, sendingApp, sendingFacility, receivingApp, receivingFacility, messageControlId, processingId)
                hl7.set_MSH("Maquina1App", "IS Hospital", "Maquina2App", "IS Exam Center", str(idListaTrabalho_Pedido), "P")
                # set_PID(self, patientIdExternal, patientIdInternal, patientName, adminisSex, patientAddress, phNumberHome, phNumberWork, mariStatus, ssnNumber, citizenship, nationality):
                hl7.set_PID(idUtente, idUtente, utente.nome, utente.sexo, utente.morada, utente.telefoneCasa, utente.telefoneTrabalho, utente.estadoCivil, utente.ssn, utente.cidadania, utente.nacionalidade)
                # set_PV1(self, sequenceId, attendingDoctor, admitTime)
                hl7.set_PV1(consulta.idConsulta, consulta.nomeMedico, consulta.data.replace('-', ''))
                # set_ORC(self, orderControl)
                hl7.set_ORC(estado, "")
                # set_OBR(self, idExame, exameCodigo, clinicalInfo)
                if idExame is None:
                    hl7.set_OBR("NULL", exameCodigo, informacaoClinicaExtra)
                else:
                    hl7.set_OBR(idExame, "NULL", "NULL")

                hl7.validate()

                print(hl7.print())

                self.cs.connect((self.host, self.porta))

                self.cs.send(hl7.getValue().encode('utf-8'))

                self.cs.close()

                self.listaTrabalhoDAO.deletePedidoByID(idListaTrabalho_Pedido)

            time.sleep(self.time)


if __name__ == "__main__":
    worklist = ListaTrabalho_PedidoThread()
    worklist.run()
