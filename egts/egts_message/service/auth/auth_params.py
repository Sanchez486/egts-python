"""EGTS_SR_AUTH_PARAMS"""
from ....egts_types import *


class AuthParams(EGTSRecord):
    """EGTS_SR_AUTH_PARAMS Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(AuthParams, self).__init__(
            ('flags', Flags()),
            # All fields are optional by default
            ('pkl', UShort(optional=True)),
            ('pbk', ArrayOfType(of_type=Byte, maxlen=512, optional=True)),
            ('isl', UShort(optional=True)),
            ('msz', UShort(optional=True)),
            ('ss', String(maxlen=255, optional=True)),
            ('d1', Byte(optional=True)),
            ('exp', String(maxlen=255, optional=True)),
            ('d2', Byte(optional=True)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        flags = self['flags']
        flags['isle'] = int(self['isl'].specified)
        flags['exe'] = int(self['exp'].specified)
        flags['sse'] = int(self['ss'].specified)
        flags['pke'] = int(self['pbk'].specified)
        flags['mse'] = int(self['msz'].specified)

        if self['ss'].specified:
            self['d1'] = 0
        if self['exp'].specified:
            self['d2'] = 0
        if self['pbk'].specified:
            self['pkl'] = len(self['pbk'])


class Flags(BitField):
    """EGTS_SR_AUTH_PARAMS Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Flags, self).__init__(
            ('empty', Bits(maxlen=1, value=0)),
            # Flags calculated based on fields existence
            ('exe', Bits(maxlen=1)),
            ('sse', Bits(maxlen=1)),
            ('mse', Bits(maxlen=1)),
            ('isle', Bits(maxlen=1)),
            ('pke', Bits(maxlen=1)),
            # No encryption by default
            ('ena', Bits(maxlen=2, value=0b01)),
            *args, **kwargs
        )
