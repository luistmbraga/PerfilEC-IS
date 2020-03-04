from hl7apy import core
from hl7apy.consts import VALIDATION_LEVEL
import time

hl7 = core.Message("ORM_O01", validation_level=VALIDATION_LEVEL.STRICT)

# Message Header    https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/MSH
hl7.msh.msh_3 = "Maquina1App"     # sending app           227
hl7.msh.msh_4 = "IS Hospital"     # sending facility      227
hl7.msh.msh_5 = "Maquina2App"     # receiving app         227
hl7.msh.msh_6 = "IS Hospital"     # receiving facility    227
hl7.msh.msh_9 = "ORM^O01"         # message type          15
hl7.msh.msh_10 = "id" #str(idWorkList) message control id   199
hl7.msh.msh_11 = "P"              # processing id         3        https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0103

# PID   https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/PID

hl7.add_group("ORM_O01_PATIENT")
hl7.ORM_O01_PATIENT.pid.pid_2 =  "1" #str(Doente_idDoente)     # patient id (external) 20   x
hl7.ORM_O01_PATIENT.pid.pid_3 = "1" #str(patient[1])           # patient id (internal) 250  x
hl7.ORM_O01_PATIENT.pid.pid_5 = "Manuel Pereira de Castro" #str(patient[2])           # patient name          250 x
hl7.ORM_O01_PATIENT.pid.pid_8 = "M"                                 # Administrative Sex    1  x     https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0001
hl7.ORM_O01_PATIENT.pid.pid_11 = "Rua do Cais nº27" #str(patient[3])          # patient address       250 x
hl7.ORM_O01_PATIENT.pid.pid_13 = "253111111" #str(patient[4])          # phone number(home)    250 x
hl7.ORM_O01_PATIENT.pid.pid_14 = "253222222"                           # phone number(busi)    250 x
hl7.ORM_O01_PATIENT.pid.pid_16 = "M"                                   # Marital Status        705  x   https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0002
hl7.ORM_O01_PATIENT.pid.pid_19 = "123456789"                           #  SSN Number - Patient 16 x
hl7.ORM_O01_PATIENT.pid.pid_26 = "Portuguesa"                          # Citizenship           705 x
hl7.ORM_O01_PATIENT.pid.pid_28 = "Portuguesa"                          # Nationality           705 x


hl7.ORM_O01_PATIENT.add_group("ORM_O01_PATIENT_VISIT")
hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.add_segment("PV1")    # PV1   https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/PV1
hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_1 = "1"       # sequence id       4
hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_2 = ""       # patient class     1 https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0004
hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_7 = "João Bastos"       # Attending Doctor	250
hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_44 = "20200228"      # Admit Date/Time	    24

# ORC   https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/ORC

hl7.ORM_O01_ORDER.orc.orc_1 = "NW" # NW CA OK         # order control         2     https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0119
# hl7.ORM_O01_ORDER.ORC.orc_2 = "1234"         # placer order number 427   https://hl7-definition.caristix.com/v2/HL7v2.6/Fields/ORC.2
# hl7.ORM_O01_ORDER.ORC.orc_9 = "20200226"    # date of transaction   24  https://hl7-definition.caristix.com/v2/HL7v2.6/DataTypes/DT



hl7.ORM_O01_ORDER.add_group("ORM_O01_ORDER_DETAIL")
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.add_segment("ORM_O01_OBSERVATION")
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.add_segment("ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP")

hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.add_segment("OBR")            # OBR   https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/OBR
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.OBR.obr_2 = "idExame"         # Placer Order Number	427
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.OBR.obr_4 = "estomatologia"       # Universal Service Identifier	                        705
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.OBR.obr_13 = "informacao clinica extra"      # 13 Relevant Clinical Information 300

hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.add_segment("RQD")            # obrigatorio (RQD contains the detail for each requisitioned item. ) https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/RQD

hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.add_segment("RQ1")            # obrigatorio (RQ1 contains additional detail for each non-stock requisitioned item. This segment definition is paired with a preceding RQD segment. ) https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/RQ1

hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.add_segment("RXO")            # obrigatorio https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/RXO

hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.add_segment("ODS")            # obrigatorio https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/ODS
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.ODS.ods_1 = ""                # obrigatorio   type                                    1   https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0159
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.ODS.ods_3 = ""                # obrigatorio   Diet, Supplement, or Preference Code    250

hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.add_segment("ODT")            # obrigatorio   https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/ODT
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP.ODT.odt_1 = ""                # obrigatorio   tray type                               250 https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0160

# talvez não colocar OBX na mensagem de pedido de exame e coloca-se o pedido de exame na seccao 13 do OBR

hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.add_segment("OBX")                           # OBX  https://hl7-definition.caristix.com/v2/HL7v2.6/Segments/OBX
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.OBX.obx_3 = "observation identifier"         # obrigatorio observation identifier    705
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.OBX.obx_5 = "relatorio"   # observation value                     99999
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.OBX.obx_11 = "T"                             # obrigatorio Observation Result Status 1       https://hl7-definition.caristix.com/v2/HL7v2.6/Tables/0085
# hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.OBX.obx_15 = "1234"                          # producer's ID    705


assert hl7.validate() is True

print(hl7.value.replace('\r', '\n'))



#import webbrowser

#webbrowser.open_new(r'file://D:\IS\FE01\AEBD_PROJECT.pdf')

