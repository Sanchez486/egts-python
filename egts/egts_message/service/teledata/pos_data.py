"""EGTS_SR_POS_DATA"""
from ....egts_types import *


class PosData(EGTSRecord):
    """EGTS_SR_POS_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(PosData, self).__init__(
            # All set outside
            ('ntm', UInt()),
            ('lat', UInt()),
            ('long', UInt()),
            ('flags', Flags()),
            ('spdl', Byte()),
            ('dirh_alts_spdh', DirhAltsSpdh()),
            ('dirl', Byte()),
            ('odm', ArrayOfType(of_type=Byte, maxlen=3, minlen=3)),
            ('din', Byte()),
            ('src', Byte()),
            ('alt', ArrayOfType(of_type=Byte, maxlen=3, minlen=3,
                                optional=True)),
            ('srcd', Short(optional=True)),
            *args, **kwargs
        )

    @property
    def special_inputs(self):
        return {
            'dir': self._set_dir,
            'spd': self._set_spd
        }

    def _set_dir(self, value):
        self['dirh_alts_spdh']['dirh'] = value // 2**8
        self['dirl'] = value % 2**8

    def _set_spd(self, value):
        self['dirh_alts_spdh']['spdh'] = value // 2 ** 8
        self['spdl'] = value % 2 ** 8

    def set_fields(self):
        """
        Calculate necessary fields
        """
        flags = self['flags']
        if self['alt'].specified:
            flags['alte'] = 0b1
        else:
            flags['alte'] = 0b1
            self['dirh_alts_spdh']['alts'] = 0b0


class DirhAltsSpdh(BitField):
    """EGTS_SR_POS_DATA Dir and Speed High bits + Altitude Sign"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(DirhAltsSpdh, self).__init__(
            ('dirh', Bits(maxlen=1)),
            ('alts', Bits(maxlen=1)),
            ('spdh', Bits(maxlen=6)),
            *args, **kwargs
        )


class Flags(BitField):
    """EGTS_SR_POS_DATA Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Flags, self).__init__(
            ('alte', Bits(maxlen=1)),
            ('lohs', Bits(maxlen=1)),
            ('lahs', Bits(maxlen=1)),
            ('mv', Bits(maxlen=1)),
            ('bb', Bits(maxlen=1)),
            ('cs', Bits(maxlen=1)),
            ('fix', Bits(maxlen=1)),
            ('vld', Bits(maxlen=1)),
            *args, **kwargs
        )
