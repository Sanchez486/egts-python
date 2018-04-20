"""EGTS_SR_ABS_LOOPIN_DATA"""
from ....egts_types import *


class AbsLoopinData(EGTSRecord):
    """EGTS_SR_ABS_LOOPIN_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(AbsLoopinData, self).__init__(
            # All set outside
            ('linl_lis', LinlLis()),
            ('linh', Byte()),
            *args, **kwargs
        )


class LinlLis(BitField):
    """EGTS_SR_ABS_LOOPIN_DATA Sensor State Bits and Number Low Bits Field"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(LinlLis, self).__init__(
            ('linl', Bits(maxlen=4)),
            ('lis', Bits(maxlen=4)),
            *args, **kwargs
        )
