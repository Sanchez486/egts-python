"""Transport Layer encoder"""
from ..egts_types import *


class Transport(EGTSRecord):
    """Transport Layer Message"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Transport, self).__init__(
            ('prv', Byte(value=0x01)),
            # no security key by default
            ('skid', Byte(value=0x00)),
            ('flags', Flags()),
            # length is unknown yet
            ('hl', Byte()),
            # header encoding is 0 by default
            ('he', Byte(value=0)),
            # No frame data yet
            ('fdl', UShort(value=0x0000)),
            # packet id = 1 by default
            ('pid', UShort(value=1)),
            ('pt', Byte()),
            ('pra', UShort(optional=True)),
            ('rca', UShort(optional=True)),
            ('ttl', Byte(optional=True)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        if (self['pra'].specified and
                self['rca'].specified and
                self['ttl'].specified):
            self['rte'] = 0b1
        elif (not self['pra'].specified and
              not self['rca'].specified and
              not self['ttl'].specified):
            self['rte'] = 0b0
        else:
            raise TypeError('Please set all address fields!')

        # Counting length; hl = length of transport layer msg + 1 byte checksum
        self['hl'] = self.__len__() + 1


class Flags(BitField):
    """Transport Layer Flags"""

    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Flags, self).__init__(
            ('prf', Bits(maxlen=2, value=0b00)),
            # address flag
            ('rte', Bits(maxlen=1)),
            # no encryption by default
            ('ena', Bits(maxlen=2, value=0b00)),
            # no compression by default
            ('cmp', Bits(maxlen=1, value=0b0)),
            # highest priority by default (?)
            ('pr', Bits(maxlen=2, value=0b00)),
            *args, ** kwargs
        )
