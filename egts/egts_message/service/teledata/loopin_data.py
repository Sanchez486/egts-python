"""EGTS_SR_LOOPIN_DATA"""
from ....egts_types import *
from . import presence_flags


class LoopinData(EGTSRecord):
    """EGTS_SR_LOOPIN_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(LoopinData, self).__init__(
            # Flags calculated based on fields existance
            ('life_flags', presence_flags.PresenceFlags(field_name='life')),
            # Flags are calculated based on fields existence
            ('lis', ArrayOfType(of_type=Lis, maxlen=4, optional=True)),
            *args, **kwargs
        )


class Lis(BitField):
    """EGTS_SR_LOOPIN_DATA Loop In State (4 bits each)"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Lis, self).__init__(
            # Flags calculated based on fields existance
            ('lis_odd', Bits(maxlen=4)),
            ('lis_even', Bits(maxlen=4)),
            *args, **kwargs
        )
