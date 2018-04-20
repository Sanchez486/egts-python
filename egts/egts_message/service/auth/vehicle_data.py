"""EGTS_SR_VEHICLE_DATA"""
from ....egts_types import *


class VehicleData(EGTSRecord):
    """EGTS_SR_VEHICLE_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(VehicleData, self).__init__(
            # VIN. Set Outside.
            ('vin', String(maxlen=17, minlen=17)),
            # Vehicle Type. Set Outside.
            ('vht', UInt()),
            # Propulsion Storage Type. Set Outside.
            ('vpst', UInt()),
            *args, **kwargs
        )
