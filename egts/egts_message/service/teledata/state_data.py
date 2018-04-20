"""EGTS_SR_STATE_DATA"""
from ....egts_types import *


class StateData(EGTSRecord):
    """EGTS_SR_STATE_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(StateData, self).__init__(
            # State is set outside
            ('st', Byte()),
            # Voltages are set outside
            ('mpsv', Byte()),
            ('bbv', Byte()),
            ('ibv', Byte()),
            ('flags', Flags()),
            *args, **kwargs
        )


class Flags(BitField):
    """EGTS_SR_STATE_DATA Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Flags, self).__init__(
            # All the state flags are set outside
            ('empty', Bits(maxlen=5, value=0)),
            ('nms', Bits(maxlen=1)),
            ('ibu', Bits(maxlen=1)),
            ('bbu', Bits(maxlen=1)),
            *args, **kwargs
        )
