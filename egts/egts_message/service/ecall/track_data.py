"""EGTS_SR_TRACK_DATA"""
from ....egts_types import *


class TrackData(EGTSRecord):
    """EGTS_SR_TRACK_DATA Class"""
    def __init__(self, *args, **kwargs):
        super(TrackData, self).__init__(
            # Structures amount is calculated based on length of tds
            ('sa', Byte()),
            # Time is set outside
            ('atm', UInt()),
            ('tds', ArrayOfType(maxlen=255, of_type=TrackDataStructure)),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
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
            ('dir', Byte(optional=True)),
            *args, ** kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        flags = self['flags']
        if (self['lat'].specified and self['long'].specified and
                self['spdl'].specified and self['dirh_spdh'].specified and
                self['dir'].specified):
            flags['tnde'] = 1
        elif (self['lat'].specified or self['long'].specified or
              self['sdpl'].specified or self['dirh_spdh'].specified or
              self['dir'].specified):
            raise NotImplementedError('Track Data is incomplete!')
        else:
            flags['tnde'] = 0


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
