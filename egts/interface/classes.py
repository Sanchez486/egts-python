"""Classes and accoridng codes"""
from ..egts_message.service import *


packet_types = {
    0: EGTSResponse,
    1: EGTSAppdata,
    2: EGTSSignedAppdata
}

subrecord_types = {
    0: RecordResponse,
    # Auth
    1: TermIdentity,
    2: ModuleData,
    3: VehicleData,
    6: AuthParams,
    7: AuthInfo,
    8: ServiceInfo,
    9: ServiceInfo,
    # Commands
    51: CommandData,
    # Firmware
    33: ServicePartData,
    34: ServiceFullData,
    # ECall
    20: AccelData,
    40: RawMsdData,
    62: TrackData,
    # Teledata
    16: PosData,
    17: ExtPosData,
    18: AdSensorsData,
    19: CountersData,
    21: StateData,
    22: LoopinData,
    23: AbsDigSensData,
    24: AbsAnSensData,
    25: AbsCntrData,
    26: AbsLoopinData,
    27: LiquidLevelSensor,
    28: PassengersCounters
}
