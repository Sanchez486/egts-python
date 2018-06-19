"""EGTS_SR_TRACK_DATA"""
from ....egts_types import *
from ....egts_types.date_time_field import DateTime


class TrackData(EGTSRecord):
    """EGTS_SR_TRACK_DATA Class"""
    def __init__(self, *args, **kwargs):
        super(TrackData, self).__init__(
            # Structures amount is calculated based on length of tds
            ('sa', Byte()),
            # Time is set outside
            ('atm', DateTime()),
            ('tds', ArrayOfType(maxlen=255, of_type=TrackDataStructure)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        if self['tds'].quantity == 0:
            self['tds'].append({'flags': {'rtm': 0, 'lohs': 0, 'lahs': 0}})
        self['sa'] = self['tds'].quantity


class TrackDataStructure(EGTSRecord):
    """EGTS_SR_TRACK_DATA Track Data Structure Field"""
    def __init__(self, *args, **kwargs):
        super(TrackDataStructure, self).__init__(
            # All track data is set outside
            ('flags', Flags()),
            ('lat', UInt(optional=True)),
            ('long', UInt(optional=True)),
            ('spdl', Byte(optional=True)),
            ('dirh_spdh', DirhSpdh(optional=True)),
            ('dirl', Byte(optional=True)),
            *args, ** kwargs
        )

    @property
    def special_inputs(self):
        return {
            'dir': self._set_dir,
            'spd': self._set_spd,
            'lat': self._set_lat,
            'long': self._set_long
        }

    @staticmethod
    def is_dig(val):
        try:
            float(str(val))
            return True
        except ValueError:
            return False

    def _set_lat(self, value):
        if self.is_dig(value):
            val = float(value)
            self['lahs'] = val >= 0
            self.value['lat'].value = int(abs(val) / 90 * 0xFFFFFFFF)
        else:
            self.value['lat'].value = value

    def _set_long(self, value):
        if self.is_dig(value):
            val = float(value)
            self['lohs'] = val >= 0
            self.value['long'].value = int(abs(val) / 180 * 0xFFFFFFFF)
        else:
            self.value['long'].value = value

    def _set_dir(self, value):
        self['dirh_spdh']['dirh'] = value // 2**8
        self['dirl'] = value % 2**8

    def _set_spd(self, value):

        self['dirh_spdh']['spdh'] = int(value) // 2 ** 8
        self['spdl'] = int(value) % 2 ** 8

    def set_fields(self):
        """
        Calculate necessary fields
        """
        flags = self['flags']
        if (self['lat'].specified and self['long'].specified and
                self['spdl'].specified and self['dirh_spdh'].specified and
                self['dirl'].specified):
            flags['tnde'] = 1
        elif (self['lat'].specified or self['long'].specified or
              self['spdl'].specified or self['dirh_spdh'].specified or
              self['dirl'].specified):
            raise NotImplementedError('Track Data is incomplete!')
        else:
            flags['tnde'] = 0
            flags['lahs'] = 0
            flags['lohs'] = 0


class Flags(BitField):
    """EGTS_SR_TRACK_DATA Track Data Structure Field Flags"""
    def __init__(self, *args, **kwargs):
        super(Flags, self).__init__(
            # Existence field is calculated based on all fields presence
            ('tnde', Bits(maxlen=1)),
            # Hemispheres and time are set outside
            ('lohs', Bits(maxlen=1)),
            ('lahs', Bits(maxlen=1)),
            ('rtm', Bits(maxlen=5)),
            *args, ** kwargs
        )


class DirhSpdh(BitField):
    """EGTS_SR_TRACK_DATA Track Data Structure Field Dir and Spd High Bits"""
    def __init__(self, *args, **kwargs):
        super(DirhSpdh, self).__init__(
            # Dir and Speed bits are set outside
            ('dirh', Bits(maxlen=1)),
            ('spdh', Bits(maxlen=7)),
            *args, ** kwargs
        )
