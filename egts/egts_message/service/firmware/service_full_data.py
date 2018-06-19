"""EGTS_SR_SERVICE_FULL_DATA"""
from ....egts_types import *
from .... import crc
from . import object_data_header


class ServiceFullData(EGTSRecord):
    """EGTS_SR_SERVICE_FULL_DATA_CLASS"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(ServiceFullData, self).__init__(
            # Header is unspecified by default
            ('odh', object_data_header.ObjectDataHeader()),
            # Data always exists and at least 1 Byte
            ('od', ArrayOfType(of_type=Byte, maxlen=65400)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        self['odh']['wos'] = crc.data_crc(self['od'].bytes)
