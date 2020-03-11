import socket

from Maquina1.Persistence.ExameDAO import ExameDAO
from hl7apy.parser import parse_message


class Server:
    def __init__(self):
        self.exameDAO = ExameDAO()
        self.ss = socket.socket()
        localhost = socket.gethostname()
        port = 3001
        self.ss.bind(('', port))

    def run(self):
        print("Maquina1 Server activo !")
        while True:
            self.__init__()

            self.ss.listen(1)
            conn, addr = self.ss.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(4026)
                hl7 = parse_message(data.decode('utf-8'))

                messageType = hl7.msh.msh_9.value

                if messageType == "ORM^O01":
                    idExame = hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.OBR.obr_2.value
                    idConsulta = hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_1.value

                    estado = hl7.ORM_O01_ORDER.orc.orc_1.value


                    if self.exameDAO.exameNotExists(idConsulta, idExame):
                        relatorio = hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.OBX.obx_5.value
                        infoClinica = hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.OBR.obr_13.value
                        exameCodigo = hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.OBR.obr_4.value

                        self.exameDAO.insertExame(idExame, idConsulta, estado, relatorio, infoClinica, exameCodigo)
                    else:
                        if estado == "SC":
                            relatorio = hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.OBX.obx_5.value
                            self.exameDAO.updateEstadoExameRela(idExame, "CM", relatorio)
                        else:
                            self.exameDAO.updateEstadoExame(idExame, estado)
                else:
                    idExame = hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.OBR.obr_2.value
                    relatorio = hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_5.value

                    self.exameDAO.updateEstadoExameRela(idExame, "CM", relatorio)



if __name__ == "__main__":
    server = Server()
    server.run()
