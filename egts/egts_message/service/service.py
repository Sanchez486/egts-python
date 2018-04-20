"""EGTS Service Layer Message Types"""
import abc
from ...egts_types import *
from .data_record import ServiceDataRecord


class EGTSService(EGTSRecord):
    """EGTS Service base class"""
    __metaclass__ = abc.ABCMeta

    def set_fields(self):
        """
        Calculate necessary fields
        """
        i = 1
        for record in self['sdr']:
            record['rn'] = i
            i += 1


class EGTSResponse(EGTSService):
    """EGTS_PT_RESPONSE"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(EGTSResponse, self).__init__(
            ('rpid', UShort()),
            ('pr', Byte()),
            ('sdr', ArrayOfType(of_type=ServiceDataRecord, maxlen=7279)),
            *args, **kwargs
        )


class EGTSAppdata(EGTSService):
    """EGTS_PT_APPDATA"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(EGTSAppdata, self).__init__(
            ('sdr', ArrayOfType(of_type=ServiceDataRecord, maxlen=7279)),
            *args, **kwargs
        )


class EGTSSignedAppdata(EGTSService):
    """EGTS_PT_SIGNED_APPDATA"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(EGTSSignedAppdata, self).__init__(
            ('sigl', UShort()),
            ('sigd', ArrayOfType(of_type=Byte, maxlen=512)),
            ('sdr', ArrayOfType(of_type=ServiceDataRecord, maxlen=7279)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        super(EGTSSignedAppdata, self).set_fields()
        self['sigl'] = len(self['sigd'])
