"""Service Data Subrecord"""
from ...egts_types import *


class ServiceDataSubRecord(EGTSRecord):
    """Subrecord of Service Data Record"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(ServiceDataSubRecord, self).__init__(
            ('srt', Byte()),
            ('srl', UShort()),
            # Unspecified by default. Set outside
            ('srd', None),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        self['srl'] = len(self['srd'])
