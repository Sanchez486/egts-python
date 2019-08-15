from egts.egts_types import *
from .wialon_types import *


class PosInfoBlock(EGTSRecord):
    """
    Wialon Message Header Class
    """
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(PosInfoBlock, self).__init__(
            ('long', Double()),
            ('lat', Double()),
            ('alt', Double()),
            ('speed', ShortBE()),
            ('dir', ShortBE()),
            ('satellites', Byte()),
            *args, **kwargs
        )
