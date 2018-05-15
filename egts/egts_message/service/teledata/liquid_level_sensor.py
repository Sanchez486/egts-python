"""EGTS_SR_LIQUID_SENSOR"""
from ....egts_types import *


class LiquidLevelSensor(EGTSRecord):
    """EGTS_SR_LIQUID_SENSOR Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(LiquidLevelSensor, self).__init__(
            ('flags', Flags()),
            # All set outside
            ('maddr', UShort()),
            ('llsd', ArrayOfType(of_type=Byte, maxlen=512, minlen=4)),
            *args, **kwargs
        )


class Flags(BitField):
    """EGTS_SR_LIQUID_SENSOR Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Flags, self).__init__(
            ('empty', Bits(maxlen=1, value=0b0)),
            # No error by default
            ('llsef', Bits(maxlen=1, value=0b0)),
            # Value unit is set outside
            ('llsvu', Bits(maxlen=2)),
            # UInt by default
            ('rdf', Bits(maxlen=1, value=0b0)),
            # Number is set outside
            ('llsn', Bits(maxlen=3)),
            *args, **kwargs
        )
