"""EGTS_SR_CNTR_DATA"""
from ....egts_types import *


class AbsCntrData(EGTSRecord):
    """EGTS_SR_CNTR_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(AbsCntrData, self).__init__(
            # Counter number and value are set outside
            ('cn', Byte()),
            ('cnv', ArrayOfType(of_type=Byte, maxlen=3, minlen=3)),
            *args, **kwargs
        )
