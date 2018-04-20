"""EGTS_SR_SERVICE_PART_DATA"""
from ....egts_types import *
from .... import crc
from . import object_data_header


class ServicePartData(EGTSRecord):
    """EGTS_SR_SERVICE_PART_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(ServicePartData, self).__init__(
            # ID is set and incremented outside.
            ('id', UShort()),
            # Part number is set and incremented outside
            ('pn', UShort()),
            # Quantity is calculated set outside
            ('epq', UShort()),
            # Header is unspecified by default
            ('odh', object_data_header.ObjectDataHeader(optional=True)),
            # Data always exists and at least 1 Byte
            ('od', ArrayOfType(of_type=Byte, maxlen=65400)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        self['odh']['wos'] = crc.data_crc(self['od'].bytes())
