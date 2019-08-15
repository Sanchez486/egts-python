from egts.egts_types import *
from .wialon_types import *
from . import header
from . import block
from .posinfo_block import PosInfoBlock


class WialonMessage(EGTSRecord):
    """
    Wialon Message Class
    """
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(WialonMessage, self).__init__(
            ('header', header.Header()),
            ('blocks', ArrayOfType(maxlen=7279, of_type=block.Block)),
            *args, **kwargs
        )

    @property
    def _data_types(self):
        return {
            'string': (1, StringZero),
            'posinfo': (2, PosInfoBlock),
            'int': (3, IntBE),
            'double': (4, Double),
            'long': (5, LongBE)
        }

    def add_block(self, block_name, data_type, *args, **kwargs):
        blocks = self['blocks']
        blocks.append()
        block_number = blocks.quantity - 1
        blk = blocks[block_number]

        type_tuple = self._data_types[data_type]
        block_type = type_tuple[0]
        data_class = type_tuple[1]
        blk['name'] = block_name
        blk['data_type'] = block_type
        blk['data'] = data_class(*args, **kwargs)
        return blk

    def get_block(self, name):
        for blk in self['blocks'].fields:
            if blk['name'].value == name:
                return blk

    def set_fields(self):
        hdr = self['header']
        hdr['packet_size'] = len(self) - len(hdr['packet_size'])


class DataType(object):
    def __init__(self, name, data_type):
        self._name = name
        self._data_type = data_type

    def get_type(self):
        return self._data_type

    def get_name(self):
        return self._name
