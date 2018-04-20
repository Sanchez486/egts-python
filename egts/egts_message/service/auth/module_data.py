"""EGTS_SR_MODULE_DATA"""
from ....egts_types import *


class ModuleData(EGTSRecord):
    """EGTS_SR_MODULE_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(ModuleData, self).__init__(
            # Module Type; Main Module by default
            ('mt', Short(value=1)),
            # Vendor ID. Set outside
            ('vid', UInt()),
            # Firmware Version. Set Outside
            ('fwv', UShort()),
            # Software version. Set Outside
            ('swv', UShort()),
            # Modification Code. Set Outside
            ('md', Byte()),
            # State is ON by default
            ('st', Byte(value=1)),
            # String fields are unspecified by default
            ('srn', String(maxlen=32, optional=True)),
            ('d1', Byte(value=0)),
            ('dscr', String(maxlen=32, optional=True)),
            ('d2', Byte(value=0)),
            *args, **kwargs
        )
