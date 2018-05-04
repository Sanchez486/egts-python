"""Service Data Record"""
from ...egts_types import *
from ...egts_types.date_time_field import DateTime
from .data_subrecord import ServiceDataSubRecord


class ServiceDataRecord(EGTSRecord):
    """Service Layer Data Record"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(ServiceDataRecord, self).__init__(
            # record length is unknown yet
            ('rl', UShort()),
            # Record number is 1 by default
            ('rn', UShort(value=0x01)),
            ('rfl', Flags()),
            # Those three fields are unspecified by default
            ('oid', UInt(optional=True)),
            ('evid', UInt(optional=True)),
            ('tm', DateTime(optional=True)),
            # Service ID's. Set outside?
            ('sst', Byte()),
            ('rst', Byte()),
            ('rd', ArrayOfType(maxlen=7279, of_type=ServiceDataSubRecord)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        self['tmfe'] = int(self['tm'].specified)
        self['evfe'] = int(self['evid'].specified)
        self['obfe'] = int(self['oid'].specified)

        self['rl'] = len(self['rd'])


class Flags(BitField):
    """Service Data Record Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Flags, self).__init__(
            # SSOD and RSOD unknown by default
            ('ssod', Bits(maxlen=1)),
            ('rsod', Bits(maxlen=1)),
            # Priority is highest by default
            ('rpp', Bits(maxlen=3, value=0)),
            # Presence flags
            ('tmfe', Bits(maxlen=1)),
            ('evfe', Bits(maxlen=1)),
            ('obfe', Bits(maxlen=1)),
            *args, **kwargs
        )
