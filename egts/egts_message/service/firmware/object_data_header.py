"""EGTS_SR_OBJECT_DATA_HEADER"""
from ....egts_types import *


class ObjectDataHeader(EGTSRecord):
    """EGTS_SR_OBJECT_DATA_HEADER Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(ObjectDataHeader, self).__init__(
            # Types are set outside
            ('oa', ObjectAttribute()),
            # ID is set outside
            ('cmi', Byte()),
            # Version is set outside
            ('ver', UShort()),
            # Checksum (CRC16-CCITT)
            ('wos', UShort()),
            # Filename is unspecified by default
            ('fn', String(maxlen=64, optional=True)),
            ('d', Byte(value=0)),
            *args, **kwargs
        )


class ObjectAttribute(BitField):
    """EGTS_SR_OBJECT_DATA_HEADER Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(ObjectAttribute, self).__init__(
            # Types are set outside
            ('empty', Bits(maxlen=4, value=0)),
            ('ot', Bits(maxlen=2)),
            ('mt', Bits(maxlen=2)),
            *args, **kwargs
        )
