"""EGTS_SR_AUTH_INFO"""
from ....egts_types import *


class AuthInfo(EGTSRecord):
    """EGTS_SR_AUTH_INFO Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(AuthInfo, self).__init__(
            # Username and password. Set outside.
            ('unm', String(maxlen=32)),
            ('d1', Byte(value=0)),
            ('upsw', String(maxlen=32)),
            ('d2', Byte(value=0)),
            ('ss', String(maxlen=255, optional=True)),
            ('d3', Byte(optional=True)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        if self['ss'].specified:
            self['d3'] = 0
