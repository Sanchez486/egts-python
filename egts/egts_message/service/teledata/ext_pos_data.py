"""EGTS_SR_EXT_POS_DATA"""
from ....egts_types import *


class ExtPosData(EGTSRecord):
    """EGTS_SR_EXT_POS_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(ExtPosData, self).__init__(
            # Flags calculated based on fields existence
            ('flags', Flags()),
            # All fields are unspecified by default
            ('vdop', UShort(optional=True)),
            ('hdop', UShort(optional=True)),
            ('pdop', UShort(optional=True)),
            ('sat', Byte(optional=True)),
            ('ns', UShort(optional=True)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        flags = self['flags']
        flags['nsfe'] = int(self['ns'].specified)
        flags['sfe'] = int(self['ns'].specified and self['sat'].specified)
        flags['pfe'] = int(self['pdop'].specified)
        flags['hfe'] = int(self['hdop'].specified)
        flags['vfe'] = int(self['vdop'].specified)


class Flags(BitField):
    """EGTS_SR_EXT_POS_DATA Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Flags, self).__init__(
            # Flags calculated based on fields existence
            ('empty', Bits(maxlen=3, value=0)),
            ('nsfe', Bits(maxlen=1)),
            ('sfe', Bits(maxlen=1)),
            ('pfe', Bits(maxlen=1)),
            ('hfe', Bits(maxlen=1)),
            ('vfe', Bits(maxlen=1)),
            *args, **kwargs
        )
