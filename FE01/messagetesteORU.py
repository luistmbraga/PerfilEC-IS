from hl7apy import core
from hl7apy.consts import VALIDATION_LEVEL
import time

hl7 = core.Message("ORU_R01", validation_level=VALIDATION_LEVEL.STRICT)

# Message Header    https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/MSH
hl7.msh.msh_3 = "Maquina1App"     # sending app           227
hl7.msh.msh_4 = "IS Hospital"     # sending facility      227
hl7.msh.msh_5 = "Maquina2App"     # receiving app         227
hl7.msh.msh_6 = "IS Hospital"     # receiving facility    227
hl7.msh.msh_9 = "ORM^O01"         # message type          15
hl7.msh.msh_10 = "id" #str(idWorkList) message control id   199
hl7.msh.msh_11 = "P"              # processing id         3        https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0103

hl7.add_group("ORU_R01_PATIENT_RESULT")
hl7.ORU_R01_PATIENT_RESULT.add_group("ORU_R01_ORDER_OBSERVATION")
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.add_segment("OBR")
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.OBR.obr_4 = "oi"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.add_group("ORU_R01_OBSERVATION")
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.add_segment("OBX")
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX[0].obx_3 = "observation identifier"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX[0].obx_5 = "1"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX[0].obx_11 = "T"

obx = hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.value

hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX[1] = obx
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX[1].obx_3 = "observation identifier"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX[1].obx_5 = "2"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX[1].obx_11 = "T"


assert hl7.validate() is True

print(hl7.value.replace('\r', '\n'))



#import webbrowser

#webbrowser.open_new(r'file://D:\IS\FE01\AEBD_PROJECT.pdf')

