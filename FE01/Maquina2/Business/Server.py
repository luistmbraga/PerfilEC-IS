import socket

from Maquina2.Persistence.ConsultaDAO import ConsultaDAO
from Maquina2.Persistence.ExameDAO import ExameDAO
from hl7apy.parser import parse_message

from Maquina2.Persistence.ListaTrabalho_ExameDAO import ListaTrabalho_ExameDAO
from Maquina2.Persistence.UtenteDAO import UtenteDAO


class Server:
    def __init__(self):
        self.utenteDAO = UtenteDAO()
        self.consultaDAO = ConsultaDAO()
        self.exameDAO = ExameDAO()
        self.listaTrabalhoDAO = ListaTrabalho_ExameDAO()
        self.ss = socket.socket()
        localhost = socket.gethostname()
        port = 3002
        self.ss.bind(('', port))

    def run(self):
        print("Maquina2 Server activo !")
        while True:
            self.__init__()

            self.ss.listen(1)
            conn, addr = self.ss.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(4026)
                hl7 = parse_message(data.decode('utf-8'))

                idUtente = hl7.ORM_O01_PATIENT.pid.pid_2.value

                if self.utenteDAO.utenteNotExists(idUtente):
                    self.insereUt(hl7, idUtente)

                idConsulta = hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_1.value

                if self.consultaDAO.consultaNotExists(idUtente, idConsulta):
                    self.insereCon(hl7, idUtente, idConsulta)

                idExame = hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.OBR.obr_2.value

                if idExame == "NULL":
                    idExame = self.insereExa(hl7, idConsulta)
                else:
                    estado = hl7.ORM_O01_ORDER.orc.orc_1.value
                    self.exameDAO.updateEstadoExame(idExame, estado)

                self.listaTrabalhoDAO.insertNovoPedido(idExame)

    def insereUt(self, hl7, idU):
        morada = hl7.ORM_O01_PATIENT.pid.pid_11.value
        telefoneCasa = hl7.ORM_O01_PATIENT.pid.pid_13.value
        telefoneTrabalho = hl7.ORM_O01_PATIENT.pid.pid_14.value
        nome = hl7.ORM_O01_PATIENT.pid.pid_5.value
        sexo = hl7.ORM_O01_PATIENT.pid.pid_8.value
        estadoCivil = hl7.ORM_O01_PATIENT.pid.pid_16.value
        ssn = hl7.ORM_O01_PATIENT.pid.pid_19.value
        nacionalidade = hl7.ORM_O01_PATIENT.pid.pid_28.value
        cidadania = hl7.ORM_O01_PATIENT.pid.pid_26.value

        self.utenteDAO.insertUtenteComId(idU, nome, sexo, morada, telefoneCasa, telefoneTrabalho, estadoCivil, ssn,
                                         cidadania, nacionalidade)

    def insereCon(self, hl7, idU, idC):
        nomemedico = hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_7.value
        data = hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_44.value
        year = data[0:4]
        month = data[4:6]
        day = data[6:8]
        dataFormatada = year + "-" + month + "-" + day

        self.consultaDAO.insertConsultaComId(idC, idU, nomemedico, dataFormatada)

    def insereExa(self, hl7, idC):
        estado = hl7.ORM_O01_ORDER.orc.orc_1.value
        infoClinica = hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.OBR.obr_13.value
        exameCodigo = hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.OBR.obr_4.value

        return self.exameDAO.insertExameSemId(idC, estado, "NULL", infoClinica, exameCodigo)


if __name__ == "__main__":
    server = Server()
    server.run()
