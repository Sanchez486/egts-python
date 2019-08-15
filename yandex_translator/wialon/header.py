from egts.egts_types import *
from .wialon_types import *


class Header(EGTSRecord):
    """
    Wialon Message Header Class
    """
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Header, self).__init__(
            ('packet_size', UInt()),
            ('controller_id', StringZero(maxlen=1024)),
            ('time', DateTimeBE()),
            ('flags', IntBE(value=3)),
            *args, **kwargs
        )
