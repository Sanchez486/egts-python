from egts.egts_types import *
from .wialon_types import *


class Block(EGTSRecord):
    """
    Wialon Message Block Class
    """
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Block, self).__init__(
            ('type', ShortBE(value=3003)),
            ('size', IntBE()),
            ('hide_attr', Boolean(value=True)),
            ('data_type', Byte()),
            ('name', StringZero(maxlen=1024)),
            ('data', None),
            *args, **kwargs
        )

    def set_fields(self):
        self['size'] = len(self) - len(self['type']) - len(self['size'])
