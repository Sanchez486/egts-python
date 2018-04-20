"""EGTS_SR_TERM_IDENTITY"""
from ....egts_types import *


class TermIdentity(EGTSRecord):
    """EGTS_SR_TERM_IDENTITY Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(TermIdentity, self).__init__(
            # terminal identifier - set outside
            ('tid', UInt()),
            # Flags calculated based on fields existence
            ('flags', Flags()),
            # All fields unspecified by default
            ('hdid', UShort(optional=True)),
            ('imei', String(maxlen=15, minlen=15, optional=True)),
            ('imsi', String(maxlen=16, minlen=16, optional=True)),
            ('lngc', String(maxlen=3, minlen=3, optional=True)),
            ('nid', NetworkIdentifier(optional=True)),
            ('bs', UShort(optional=True)),
            ('msisdn', String(maxlen=15, minlen=15, optional=True)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        flags = self['flags']
        flags['mne'] = int(self['msisdn'].specified)
        flags['bse'] = int(self['bs'].specified)
        flags['nide'] = int(self['nid'].specified)
        flags['lngce'] = int(self['lngc'].specified)
        flags['imsie'] = int(self['imsi'].specified)
        flags['imeie'] = int(self['imei'].specified)
        flags['hdide'] = int(self['hdid'].specified)


class NetworkIdentifier(BitField):
    """EGTS_SR_TERM_IDENTITY Network Identifier Field"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(NetworkIdentifier, self).__init__(
            ('empty', Bits(maxlen=4, value=0)),
            # Mobile Codes; set outside
            ('mcc', Bits(maxlen=10)),
            ('mnc', Bits(maxlen=10)),
            *args, **kwargs
        )


class Flags(BitField):
    """EGTS_SR_TERM_IDENTITY Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Flags, self).__init__(
            # Flags calculated based on fields existence
            ('mne', Bits(maxlen=1)),
            ('bse', Bits(maxlen=1)),
            ('nide', Bits(maxlen=1)),
            # Simple algorithm by default
            ('ssra', Bits(maxlen=1, value=1)),
            ('lngce', Bits(maxlen=1)),
            ('imsie', Bits(maxlen=1)),
            ('imeie', Bits(maxlen=1)),
            ('hdide', Bits(maxlen=1)),
            *args, **kwargs
        )
