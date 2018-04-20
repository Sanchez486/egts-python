"""Whole EGTS Message"""
from . import transport
from ..egts_types import *
from .. import crc


class EGTSMessage(EGTSRecord):
    """
    EGTS message class
    """
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(EGTSMessage, self).__init__(
            ('transport', transport.Transport()),
            ('hcs', Byte()),
            ('service', None),
            ('sfrcs', UShort(optional=True)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        if self['service']:
            self['sfrcs'] = crc.data_crc(self['service'].bytes)
            self['transport']['fdl'] = len(self['service'])
        self['hcs'] = crc.header_crc(self['transport'].bytes)
