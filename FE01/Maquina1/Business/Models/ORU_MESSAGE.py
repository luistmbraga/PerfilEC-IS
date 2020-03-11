from hl7apy import core
from hl7apy.consts import VALIDATION_LEVEL


class ORU_MESSAGE:
    def __init__(self):
        self.hl7 = core.Message("ORU_R01", validation_level=VALIDATION_LEVEL.STRICT)

    def get_MSG(self):
        return self.hl7

    # https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/MSH
    def set_MSH(self, sendingApp, sendingFacility, receivingApp, receivingFacility, messageControlId, processingId):
        self.hl7.msh.msh_3 = sendingApp  # sending app           227
        self.hl7.msh.msh_4 = sendingFacility  # sending facility      227
        self.hl7.msh.msh_5 = receivingApp  # receiving app         227
        self.hl7.msh.msh_6 = receivingFacility  # receiving facility    227
        self.hl7.msh.msh_9 = "ORU^R01"  # message type          15
        self.hl7.msh.msh_10 = messageControlId  # message control id   199
        self.hl7.msh.msh_11 = processingId  # processing id         3        https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0103

    # https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/OBR
    def set_OBR(self, idExame, exameCodigo, clinicalInfo):
        self.hl7.add_group("ORU_R01_PATIENT_RESULT")
        self.hl7.ORU_R01_PATIENT_RESULT.add_group("ORU_R01_ORDER_OBSERVATION")
        self.hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.add_segment("OBR")
        self.hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.OBR.obr_2 = str(idExame)
        self.hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.OBR.obr_4 = exameCodigo
        self.hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.OBR.obr_13 = clinicalInfo
        self.hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.add_group("ORU_R01_OBSERVATION")

    # OBX  https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/OBX
    def set_OBX(self, relatorio):
        self.hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.add_segment("OBX")
        self.hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_3 = "observation identifier"
        self.hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_5 = relatorio
        self.hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_11 = "T"

    def validate(self):
        return self.hl7.validate()

    def print(self):
        return self.hl7.value.replace('\r', '\n')

    def getValue(self):
        return self.hl7.value
