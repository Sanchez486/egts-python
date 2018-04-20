"""EGTS_SR_SERVICE_INFO"""
from ....egts_types import *


class ServiceInfo(EGTSRecord):
    """EGTS_SR_SERVICE_INFO Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(ServiceInfo, self).__init__(
            ('st', Byte()),
            # Default statement is IN_SERVICE
            ('sst', Byte(value=0)),
            ('srvp', ServiceParameters()),
            *args, **kwargs
        )


class ServiceParameters(BitField):
    """EGTS_SR_SERVICE_INFO Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(ServiceParameters, self).__init__(
            # Service Attribute. Set Outside.
            ('srva', Bits(maxlen=1)),
            ('empty', Bits(maxlen=5, value=0)),
            #  Priority is highest by default
            ('srvrp', Bits(maxlen=2, value=0b00)),
            *args, **kwargs
        )
