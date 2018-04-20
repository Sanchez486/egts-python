"""EGTS_SR_AD_SENSORS_DATA"""
from ....egts_types import *
from . import presence_flags


class AdSensorsData(EGTSRecord):
    """EGTS_SR_AD_SENSORS_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(AdSensorsData, self).__init__(
            # Flags calculated based on fields existance
            ('dioe_flags', presence_flags.PresenceFlags(field_name='dioe')),
            # DOUT - set outside?
            ('dout', Byte()),
            # ASFE Flags set outside
            ('asfe_flags', presence_flags.PresenceFlags(field_name='asfe')),
            # digital inputs fields set outside
            ('adio', ArrayOfType(of_type=Byte, maxlen=8, optional=True)),
            # analog sensor fields set outside
            ('ans', ArrayOfType(of_type=Ans, maxlen=8, optional=True)),
            *args, **kwargs
        )


class Ans(ArrayOfType):
    """EGTS_SR_AD_SENSORS_DATA Additional Digital Input Class"""
    def __init__(self):
        """
        Field of 3 bytes constructor
        """
        super(Ans, self).__init__(of_type=Byte, maxlen=3, minlen=3)
