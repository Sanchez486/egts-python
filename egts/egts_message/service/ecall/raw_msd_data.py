"""EGTS_SR_RAW_MSD_DATA"""
from ....egts_types import *


class RawMsdData(EGTSRecord):
    """EGTS_SR_RAW_MSD_DATA Class"""
    def __init__(self, *args, **kwargs):
        super(RawMsdData, self).__init__(
            # Format is GOST by default
            ('fm', Byte(value=1)),
            # Data is set outside
            ('msd', ArrayOfType(of_type=Byte, maxlen=116)),
            *args, **kwargs
        )
