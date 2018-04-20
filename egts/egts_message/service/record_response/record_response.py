"""EGTS_SR_RECORD_RESPONSE. Common for every service type"""
from ....egts_types import *


class RecordResponse(EGTSRecord):
    """EGTS_SR_RECORD_RESPONSE Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(RecordResponse, self).__init__(
            ('crn', UShort()),
            ('rst', Byte()),
            *args, **kwargs
        )
