"""EGTS_SR_ACCEL_DATA"""
from ....egts_types import *


class AccelData(EGTSRecord):
    """EGTS_SR_ACCEL_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(AccelData, self).__init__(
            # Structures amount is calculated based on length of ads
            ('sa', Byte()),
            # Time is set outside
            ('atm', UInt()),
            ('ads', ArrayOfType(of_type=AccelerometerDataService, maxlen=255)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        self['sa'] = self['ads'].quantity


class AccelerometerDataService(EGTSRecord):
    """EGTS_SR_ACCEL_DATA Data Field"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(AccelerometerDataService, self).__init__(
            # Time is set outside
            ('rtm', UShort()),
            # Acceleration Values are set outside
            ('xaav', Short()),
            ('yaav', Short()),
            ('zaav', Short()),
            *args, **kwargs
        )
