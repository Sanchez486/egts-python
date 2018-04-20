"""EGTS_SR_COUNTERS_DATA"""
from ....egts_types import *
from . import presence_flags


class CountersData(EGTSRecord):
    """EGTS_SR_COUNTERS_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(CountersData, self).__init__(
            # Flags calculated based on fields existance
            ('cfe_flags', presence_flags.PresenceFlags(field_name='cfe')),
            # counter fields set outside
            ('cn', ArrayOfType(of_type=Cn, maxlen=8, optional=True)),
            *args, **kwargs
        )


class Cn(ArrayOfType):
    """EGTS_SR_COUNTERS_DATA Counter Class"""
    def __init__(self):
        """
        Field of 3 bytes constructor
        """
        super(Cn, self).__init__(of_type=Byte, maxlen=3, minlen=3)
