"""Field values enums"""
import enum
from ..egts_types import *


class Flag(enum.Enum):
    """Field Flag Bits"""
    FIELD_NOT_EXIST = 0b0
    FIELD_EXISTS = 0b1


class PacketType(enum.Enum):
    """Packet Type Field values"""
    EGTS_PT_RESPONSE = 0
    EGTS_PT_APPDATA = 1
    EGTS_PT_SIGNED_APPDATA = 2


class Priority(enum.Enum):
    """Priority Field Values"""
    HIGHEST = 0b00
    HIGH = 0b01
    MEDIUM = 0b10
    LOW = 0b11


class EncryptionAlgorithm(enum.Enum):
    """Supported Encryption Algorithm Codes"""
    NO_ENCRYPTION = 0b00


class ServiceOnDrive(enum.Enum):
    """Service location flag"""
    DEVICE_SIDE = 0b1
    PLATFORM_SIDE = 0b0


class ServiceType(enum.Enum):
    """Service Types (SST, RST)"""
    CONFIRMATION = 0
    EGTS_AUTH_SERVICE = 1
    EGTS_TELEDATA_SERVICE = 2
    EGTS_COMMANDS_SERVICE = 4
    EGTS_FIRMWARE_SERVICE = 9
    EGTS_ECALL_SERVICE = 10


class SubrecordType(enum.Enum):
    """All Subrecord Types"""
    EGTS_SR_RECORD_RESPONSE = 0
    EGTS_SR_TERM_IDENTITY = 1
    EGTS_SR_MODULE_DATA = 2
    EGTS_SR_VEHICLE_DATA = 3
    EGTS_SR_AUTH_PARAMS = 6
    EGTS_SR_AUTH_INFO = 7
    EGTS_SR_SERVICE_INFO = 8
    EGTS_SR_RESULT_CODE = 9
    EGTS_SR_COMMAND_DATA = 51
    EGTS_SR_SERVICE_PART_DATA = 33
    EGTS_SR_SERVICE_FULL_DATA = 34
    EGTS_SR_ACCEL_DATA = 20
    EGTS_SR_RAW_MSD_DATA = 40
    EGTS_SR_TRACK_DATA = 62


class LanguageCode(enum.Enum):
    """Language codes"""
    RUSSIAN = 'rus'


class ModuleType(enum.Enum):
    """Module Types for Module Data"""
    MAIN_MODULE = 1
    IO_MODULE = 2
    NAVIGATIONAL_RECEIVER_MODULE = 3
    WIRELESS_CONNECTION_MODULE = 4


class ModuleState(enum.Enum):
    """Module States"""
    ON = 1
    OFF = 0


class VehicleType(enum.Enum):
    """Vehicle Types"""
    M1_PASSENGER_CAR = 0b0001
    M2_BUS = 0b0010
    M3_BUS = 0b0011
    N1_LIGHT_TRUCK = 0b0100
    N2_HEAVY_TRUCK = 0b0101
    N3_HEAVY_TRUCK = 0b0110
    L1E_MOTO = 0b0111
    L2E_MOTO = 0b1000
    L3E_MOTO = 0b1001
    L4E_MOTO = 0b1010
    L5E_MOTO = 0b1011
    L6E_MOTO = 0b1100
    L7E_MOTO = 0b1101


class VehiclePropulsionStorageType(enum.Enum):
    """Vehicle Fuel Type; Could be set more than one type: Add the values"""
    NOT_SET = 0
    PETROL = 0b1
    DIESEL = 0b10
    COMPRESSED_NATURAL_GAS = 0b100
    LIQUIFIED_PETROLEUM_GAS = 0b1000
    ELECTRICITY = 0b10000
    HYDROGEN = 0b100000


class ServiceAttribute(enum.Enum):
    """Service Attribute (Supported/Requested)"""
    SUPPORTED_SERVICE = 0b0
    REQUESTED_SERVICE = 0b1


class ServiceStatement(enum.Enum):
    """Service Statement"""
    EGTS_SST_IN_SERVICE = 0
    EGTS_SST_OUT_OF_SERVICE = 128
    EGTS_SST_DENIED = 129
    EGTS_SST_NO_CONF = 130
    EGTS_SST_TEMP_UNAVAIL = 131


class CommandType(enum.Enum):
    """Command Type (ct)"""
    CT_COMCONF = 0b0001
    CT_MSGCONF = 0b0010
    CT_MSGFROM = 0b0011
    CT_MSGTO = 0b0100
    CT_COM = 0b0101
    CT_DELCOM = 0b0110
    CT_SUBREQ = 0b0111
    CT_DELIV = 0b1000


class CommandConfirmationType(enum.Enum):
    """Command Confirmation Type (cct)"""
    CC_OK = 0b0000
    CC_ERROR = 0b0001
    CC_ILL = 0b0010
    CC_DEL = 0b0100
    CC_NFOUND = 0b0100
    CC_NCONF = 0b0101
    CC_INPROG = 0b0110


class CharSet(enum.Enum):
    """String Encoding"""
    CP_1251 = 0
    ASCII = 1
    BINARY = 2
    LATIN_1 = 3
    JIS = 5
    CYRILLIC = 6
    LATIN_HEBREW = 7
    UCS2 = 8


class Action(enum.Enum):
    """Command action"""
    COMMAND_PARAMETERS = 0
    VALUE_REQUEST = 1
    VALUE_SET = 2
    ADD_PARAMETER = 3
    DELETE_PARAMETER = 4


class Command(enum.Enum):
    """EGTS Command"""
    EGTS_SR_RAW_DATA = 0x0000
    EGTS_TEST_MODE = 0x0001
    EGTS_CONFIG_RESET = 0x0006
    EGTS_SET_AUTH_CODE = 0x0007
    EGTS_RESTART = 0x0008
    EGTS_ECALL_REQ = 0x0112
    EGTS_ECALL_MSD_REQ = 0x00113
    EGTS_ACCEL_DATA = 0x0114
    EGTS_TRACK_DATA = 0x0115
    EGTS_ECALL_DEREGISTRATION = 0x0116


class CommandConfirmation(enum.Enum):
    """Command Confirmation"""
    EGTS_RAW_DATA = 0x0000


class ObjectType(enum.Enum):
    """Object type"""
    FIRMWARE = 0b00
    CONFIGURATION_PARAMETERS_BLOCK = 0b01


class ServiceModuleType(enum.Enum):
    """Service Module Type (Periphery/Device)"""
    PERIPHERY = 0b00
    DEVICE = 0b01


class Format(enum.Enum):
    """Format (GOST/Other)"""
    FORMAT_UNKNOWN = 0
    GOST_33464 = 1


class LatitudeHemisphere(enum.Enum):
    """Latitude Hemisphere (e/w)"""
    EASTERN = 0b0
    WESTERN = 0b1


class LongitudeHemisphere(enum.Enum):
    """Longtitude Hemisphere (n/s)"""
    NORTHERN = 0b0
    SOUTHERN = 0b1


class Result(enum.Enum):
    """Processing Result Codes"""
    EGTS_PC_OK = 0
    EGTS_PC_IN_PROGRESS = 1
    EGTS_PC_UNS_PROTOCOL = 128
    EGTS_PC_DECRYPT_ERROR = 129
    EGTS_PC_PROC_DENIED = 130
    EGTS_PC_INC_HEADERFORM = 131
    EGTS_PC_INC_DATAFORM = 132
    EGTS_PC_UNS_TYPE = 133
    EGTS_PC_NOTEN_PARAMS = 134
    EGTS_PC_DBL_PROC = 135
    EGTS_PC_PROC_SRC_DENIED = 136
    EGTS_PC_HEADERCRC_ERROR = 137
    EGTS_PC_DATACRC_ERROR = 138
    EGTS_PC_INVDATALEN = 139
    EGTS_PC_ROUTE_NFOUND = 140
    EGTS_PC_ROUTE_CLOSED = 141
    EGTS_PC_ROUTE_DENIED = 142
    EGTS_PC_INVADDR = 143
    EGTS_PC_TTLEXPIRED = 144
    EGTS_PC_NO_ACK = 145
    EGTS_PC_OBJ_NFOUND = 146
    EGTS_PC_EVENT_NFOUND = 147
    EGTS_PC_SRVC_NFOUND = 148
    EGTS_PC_SRVC_DENIED = 149
    EGTS_PC_SRVC_UNKN = 150
    EGTS_PC_AUTH_DENIED = 151
    EGTS_PC_ALREADY_EXISTS = 152
    EGTS_PC_ID_NFOUND = 153
    EGTS_PC_INC_DATETIME = 154
    EGTS_PC_IO_ERROR = 155
    EGTS_PC_NO_RES_AVAIL = 156
    EGTS_PC_MODULE_FAULT = 157
    EGTS_PC_MODULE_PWR_FLT = 158
    EGTS_PC_MODULE_PROC_FLT = 159
    EGTS_PC_MODULE_SW_FLT = 160
    EGTS_PC_MODULE_FW_FLT = 161
    EGTS_PC_MODULE_IO_FLT = 162
    EGTS_PC_MODULE_MEM_FLT = 163
    EGTS_PC_TEST_FAILED = 164


class DeviceParameterCode(enum.Enum):
    """Device Parameter Codes"""
    # Radio Mute
    EGTS_RADIO_MUTE_DELAY = 0x0201
    EGTS_RADIO_UNMUTE_DELAY = 0x0202
    # General Settings
    EGTS_GPRS_APN = 0x0203
    EGTS_SERVER_ADDRESS = 0x0204
    EGTS_SIM_PIN = 0x0205
    EGTS_INT_MEM_TRANSMIT_INTERVAL = 0x0206
    EGTS_INT_MEM_TRANSMIT_ATTEMPTS = 0x0207
    # Testing Mode
    EGTS_TEST_REGISTRATION_PERIOD = 0x0242
    EGTS_TEST_MODE_END_DISTANCE = 0x020A
    # Car Service Mode
    EGTS_GARAGE_MODE_END_DISTANCE = 0x020B
    EGTS_GARAGE_MODE_PIN = 0x020C
    # ECALL
    EGTS_ECALL_TEST_NUMBER = 0x020D
    EGTS_ECALL_ON = 0x0210
    EGTS_ECALL_CRASH_SIGNAL_INTERNAL = 0x0211
    EGTS_ECALL_CRASH_SIGNAL_EXTERNAL = 0x0212
    EGTS_ECALL_SOS_BUTTON_TIME = 0x0213
    EGTS_ECALL_NO_AUTOMATIC_TRIGGERING = 0x0214
    EGTS_ASI15_TRESHOLD = 0x0215
    EGTS_ECALL_MODE_PIN = 0x0216
    EGTS_ECALL_CCFT = 0x0217
    EGTS_ECALL_INVITATION_SIGNAL_DURATION = 0x0218
    EGTS_ECALL_SEND_MSG_PERIOD = 0x0219
    EGTS_ECALL_AL_ACK_PERIOD = 0x021A
    EGTS_ECALL_MSD_MAX_TRANSMISSION_TIME = 0x021B
    EGTS_ECALL_NAD_DEREGESTRATION_TIMER = 0x021D
    EGTS_ECALL_DIAL_DURATION = 0x021E
    EGTS_ECALL_AUTO_DIAL_ATTEMPTS = 0x021F
    EGTS_ECALL_MANUAL_DIAL_ATTEMPTS = 0x0220
    EGTS_ECALL_MANUAL_CAN_CANCEL = 0x0222
    EGTS_ECALL_SMS_FALLBACK_NUMBER = 0x0223
    # Crash Record
    INGNITION_OFF_FOLLOW_UP_TIME1 = 0x0224
    IGNITION_OFF_FOLLOW_UP_TIME2 = 0x0225
    EGTS_CRASH_RECORD_TIME = 0x0251
    EGTS_CRASH_RECORD_RESOLUTION = 0x0252
    EGTS_CRASH_PRE_RECORD_TIME = 0x0253
    EGTS_CRASH_PRE_RECORD_RESOLUTION = 0x0254
    # Crash Track Record
    EGTS_TRACK_RECORD_TIME = 0x025A
    EGTS_TRACK_PRE_RECORD_TIME = 0x025B
    EGTS_TRACK_RECORD_RESOLUTION = 0x025C
    # Other Parameters
    EGTS_GNSS_POWER_OFF_TIME = 0x0301
    EGTS_GNSS_DATA_RATE = 0x0302
    EGTS_GNSS_MIN_ELEVATION = 0x0303
    # Vehicle Parameters
    EGTS_VEHICLE_VIN = 0x0311
    EGTS_VEHICLE_PROPULSION_STORAGE_TYPE = 0x0313
    EGTS_VEHICLE_TYPE = 0x0312
    # Device Parameters
    EGTS_UNIT_ID = 0x0404
    EGTS_UNIT_IMEI = 0x0405
    EGTS_UNIT_RS485_BAUD_RATE = 0x0406
    EGTS_UNIT_RS485_STOP_BITS = 0x0407
    EGTS_UNIT_RS485_BAUD_PARITY = 0x0408
    EGTS_UNIT_HOME_DISPATCHER_ID = 0x0411
    EGTS_SERVICE_AUTH_METHOD = 0x0412
    EGTS_SERVER_CHECK_IN_PERIOD = 0x0413
    EGTS_SERVER_CHECK_IN_ATTEMPTS = 0x0414
    EGTS_SERVER_PACKET_OUT = 0x0415
    EGTS_SERVER_PACKET_RETRANSMIT_ATTEMPTS = 0x0416
    EGTS_UNIT_MIC_LEVEL = 0x0417
    EGTS_UNIT_SPK_LEVEL = 0x0418


class DeviceParameterValue(enum.Enum):
    """Device Parameter Values"""
    # Radio Mute
    EGTS_RADIO_MUTE_DELAY = Int(value=0)
    EGTS_RADIO_UNMUTE_DELAY = Int(value=0)
    # General Settings
    EGTS_GPRS_APN = String(maxlen=65200, value='')
    EGTS_SERVER_ADDRESS = String(maxlen=65200, value='')
    EGTS_SIM_PIN = Int(value=0)
    EGTS_INT_MEM_TRANSMIT_INTERVAL = Int(value=60)
    EGTS_INT_MEM_TRANSMIT_ATTEMPTS = Int(value=10)
    # Testing Mode
    EGTS_TEST_REGISTRATION_PERIOD = Int(value=5)
    EGTS_TEST_MODE_END_DISTANCE = Int(value=300)
    # Car Service Mode
    EGTS_GARAGE_MODE_END_DISTANCE = Int(value=300)
    EGTS_GARAGE_MODE_PIN = Int(value=0)
    # ECALL
    EGTS_ECALL_TEST_NUMBER = String(maxlen=65200, value='')
    EGTS_ECALL_ON = Boolean(value=True)
    EGTS_ECALL_CRASH_SIGNAL_INTERNAL = Boolean(value=True)
    EGTS_ECALL_CRASH_SIGNAL_EXTERNAL = Boolean(value=True)
    EGTS_ECALL_SOS_BUTTON_TIME = Int(value=200)
    EGTS_ECALL_NO_AUTOMATIC_TRIGGERING = Boolean(value=True)
    EGTS_ASI15_TRESHOLD = Float(value=1.8)
    EGTS_ECALL_MODE_PIN = Int(value=0)
    EGTS_ECALL_CCFT = Int(value=60)
    EGTS_ECALL_INVITATION_SIGNAL_DURATION = Int(value=2000)
    EGTS_ECALL_SEND_MSG_PERIOD = Int(value=5000)
    EGTS_ECALL_AL_ACK_PERIOD = Int(value=5000)
    EGTS_ECALL_MSD_MAX_TRANSMISSION_TIME = Int(value=20)
    EGTS_ECALL_NAD_DEREGESTRATION_TIMER = Int(value=8)
    EGTS_ECALL_DIAL_DURATION = Int(value=5)
    EGTS_ECALL_AUTO_DIAL_ATTEMPTS = Int(value=10)
    EGTS_ECALL_MANUAL_DIAL_ATTEMPTS = Int(value=10)
    EGTS_ECALL_MANUAL_CAN_CANCEL = Boolean(value=True)
    EGTS_ECALL_SMS_FALLBACK_NUMBER = String(maxlen=65200, value='112')
    # Crash Record
    INGNITION_OFF_FOLLOW_UP_TIME1 = Int(value=120)
    IGNITION_OFF_FOLLOW_UP_TIME2 = Int(value=240)
    EGTS_CRASH_RECORD_TIME = Int(value=250)
    EGTS_CRASH_RECORD_RESOLUTION = Int(value=1)
    EGTS_CRASH_PRE_RECORD_TIME = Int(value=20000)
    EGTS_CRASH_PRE_RECORD_RESOLUTION = Int(value=5)
    # Crash Track Record
    EGTS_TRACK_RECORD_TIME = Int(value=10)
    EGTS_TRACK_PRE_RECORD_TIME = Int(value=20)
    EGTS_TRACK_RECORD_RESOLUTION = Int(value=10)
    # Other Parameters
    EGTS_GNSS_POWER_OFF_TIME = Int(value=500)
    EGTS_GNSS_DATA_RATE = Int()
    EGTS_GNSS_MIN_ELEVATION = Int(value=15)
    # Vehicle Parameters
    EGTS_VEHICLE_VIN = String(maxlen=65200, value='')
    EGTS_VEHICLE_PROPULSION_STORAGE_TYPE = Int(value=0)
    EGTS_VEHICLE_TYPE = Int(value=0)
    # Device Parameters
    EGTS_UNIT_ID = Int(value=0)
    EGTS_UNIT_IMEI = String(maxlen=65200, value='')
    EGTS_UNIT_RS485_BAUD_RATE = Int(value=19200)
    EGTS_UNIT_RS485_STOP_BITS = Int(value=1)
    EGTS_UNIT_RS485_BAUD_PARITY = Int(value=0)
    EGTS_UNIT_HOME_DISPATCHER_ID = Int(value=0)
    EGTS_SERVICE_AUTH_METHOD = Int(value=1)
    EGTS_SERVER_CHECK_IN_PERIOD = Int(value=30)
    EGTS_SERVER_CHECK_IN_ATTEMPTS = Int(value=5)
    EGTS_SERVER_PACKET_OUT = Int(value=5)
    EGTS_SERVER_PACKET_RETRANSMIT_ATTEMPTS = Int(value=3)
    EGTS_UNIT_MIC_LEVEL = Int(value=8)
    EGTS_UNIT_SPK_LEVEL = Int(value=6)
