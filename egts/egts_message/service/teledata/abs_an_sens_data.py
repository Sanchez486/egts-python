"""EGTS_SR_ABS_AN_SENS_DATA"""
from ....egts_types import *


class AbsAnSensData(EGTSRecord):
    """EGTS_SR_ABS_AN_SENS_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(AbsAnSensData, self).__init__(
            # Analog Sensor state and number are set outside
            ('asn', Byte()),
            ('asv', ArrayOfType(of_type=Byte, maxlen=3, minlen=3)),
            *args, **kwargs
        )
