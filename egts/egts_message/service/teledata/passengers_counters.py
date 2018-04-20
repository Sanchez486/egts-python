"""EGTS_SR_PASSENGERS_COUNTERS"""
from ....egts_types import *
from . import presence_flags


class PassengersCounters(EGTSRecord):
    """EGTS_SR_PASSENGERS_COUNTERS Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(PassengersCounters, self).__init__(
            # All set outside
            ('flags', Flags()),
            ('dpr', presence_flags.PresenceFlags(field_name='dpr')),
            ('drl', presence_flags.PresenceFlags(field_name='drl')),
            ('maddr', UShort()),
            ('pcd', ArrayOfType(of_type=Pcd, maxlen=8, fixed=1)),
            *args, **kwargs
        )


class Flags(BitField):
    """EGTS_SR_PASSENGERS_COUNTERS Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Flags, self).__init__(
            ('empty', Bits(maxlen=7, value=0)),
            ('rdf', Bits(maxlen=1)),
            *args, **kwargs
        )


class Pcd(ArrayOfType):
    """EGTS_SR_PASSENGERS_COUNTERS Passenger Counters Data"""
    def __init__(self):
        super(Pcd, self).__init__(of_type=Byte, maxlen=2, minlen=2)
