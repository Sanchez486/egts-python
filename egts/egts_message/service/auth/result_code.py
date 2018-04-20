"""EGTS_SR_RESULT_CODE"""
from ....egts_types import *


class ResultCode(EGTSRecord):
    """EGTS_SR_RESULT_CODE Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(ResultCode, self).__init__(
            # Result code. Set Outside.
            ('rcd', Byte()),
            *args, **kwargs
        )
