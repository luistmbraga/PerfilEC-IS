from hl7apy import core
from hl7apy.consts import VALIDATION_LEVEL

class ORM_MESSAGE:
    def __init__(self):
        self.hl7 = core.Message("ORM_O01", validation_level=VALIDATION_LEVEL.STRICT)

    def get_MSG(self):
        return self.hl7

    # https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/MSH
    def set_MSH(self, sendingApp, sendingFacility, receivingApp, receivingFacility, messageControlId, processingId):
        self.hl7.msh.msh_3 = sendingApp         # sending app           227
        self.hl7.msh.msh_4 = sendingFacility    # sending facility      227
        self.hl7.msh.msh_5 = receivingApp       # receiving app         227
        self.hl7.msh.msh_6 = receivingFacility  # receiving facility    227
        self.hl7.msh.msh_9 = "ORM^O01"          # message type          15
        self.hl7.msh.msh_10 = messageControlId  # message control id   199
        self.hl7.msh.msh_11 = processingId      # processing id         3        https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0103

    # https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/PID
    def set_PID(self, patientIdExternal, patientIdInternal, patientName, adminisSex, patientAddress, phNumberHome, phNumberWork, mariStatus, ssnNumber, citizenship, nationality):
        self.hl7.add_group("ORM_O01_PATIENT")
        self.hl7.ORM_O01_PATIENT.pid.pid_2 = patientIdExternal      # patient id (external) 20
        self.hl7.ORM_O01_PATIENT.pid.pid_3 = patientIdInternal      # patient id (internal) 250
        self.hl7.ORM_O01_PATIENT.pid.pid_5 = patientName            # patient name          250
        self.hl7.ORM_O01_PATIENT.pid.pid_8 = adminisSex             # Administrative Sex    1     https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0001
        self.hl7.ORM_O01_PATIENT.pid.pid_11 = patientAddress        # patient address       250
        self.hl7.ORM_O01_PATIENT.pid.pid_13 = phNumberHome          # phone number(home)    250
        self.hl7.ORM_O01_PATIENT.pid.pid_14 = phNumberWork          # phone number(busi)    250
        self.hl7.ORM_O01_PATIENT.pid.pid_16 = mariStatus            # Marital Status        705     https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0002
        self.hl7.ORM_O01_PATIENT.pid.pid_19 = ssnNumber             # SSN Number - Patient 16
        self.hl7.ORM_O01_PATIENT.pid.pid_26 = citizenship           # Citizenship           705
        self.hl7.ORM_O01_PATIENT.pid.pid_28 = nationality           # Nationality           705

    # https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/PV1
    def set_PV1(self, sequenceId, attendingDoctor, admitTime):
        self.hl7.ORM_O01_PATIENT.add_group("ORM_O01_PATIENT_VISIT")
        self.hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.add_segment("PV1")           # PV1   https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/PV1
        self.hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_1 = sequenceId       # sequence id       4
        self.hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_2 = ""
        self.hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_7 = attendingDoctor  # Attending Doctor	250
        self.hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_44 = admitTime       # Admit Date/Time	    24

    # https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/ORC
    def set_ORC(self, orderControl, status):
        self.hl7.ORM_O01_ORDER.orc.orc_1 = orderControl  # order control         2     https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0119  estado
        self.hl7.ORM_O01_ORDER.orc.orc_5 = status

    # https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/OBR
    def set_OBR(self, idExame, exameCodigo, clinicalInfo):
        self.hl7.ORM_O01_ORDER.add_group("ORM_O01_ORDER_DETAIL")
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.add_segment("ORM_O01_OBSERVATION")
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.add_segment("ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP")
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.add_segment("RQD")   # obrigatorio (RQD contains the detail for each requisitioned item. ) https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/RQD
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.add_segment("RQ1")   # obrigatorio (RQ1 contains additional detail for each non-stock requisitioned item. This segment definition is paired with a preceding RQD segment. ) https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/RQ1
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.add_segment("RXO")   # obrigatorio https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/RXO
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.add_segment("ODS")   # obrigatorio https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/ODS
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.ODS.ods_1 = ""       # obrigatorio   type                                    1   https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0159
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.ODS.ods_3 = ""       # obrigatorio   Diet, Supplement, or Preference Code    250
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.add_segment("ODT")   # obrigatorio   https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/ODT
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.ODT.odt_1 = ""       # obrigatorio   tray type                               250 https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0160
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.add_segment("OBX")
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.OBX.obx_3 = "observation identifier"  # obrigatorio observation identifier    705
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.OBX.obx_11 = "T"  # obrigatorio Observation Result Status 1       https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0085
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.add_segment("OBR")           # OBR   https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/OBR
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.OBR.obr_2 = str(idExame)          # idExame
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.OBR.obr_4 = exameCodigo      # Universal Service Identifier	   exameCodigo                      705
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.OBR.obr_13 = clinicalInfo    # Relevant Clinical Information 300

    # OBX  https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/OBX
    def set_OBX(self, relatorio):
        self.hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.OBX.obx_5 = relatorio  # observation value                     99999

    def validate(self):
        return self.hl7.validate()

    def print(self):
        return self.hl7.value.replace('\r', '\n')

    def getValue(self):
        return self.hl7.value