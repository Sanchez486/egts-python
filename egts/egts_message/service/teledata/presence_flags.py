"""Unique Teledata Structure - Array of 8 flags for 8 objects"""
from ....egts_types import BitField, Bits


class PresenceFlags(BitField):
    """Presence Flags class"""
    def __init__(self, field_name, *args, **kwargs):
        """
        Adds fields name in regular BitField Object
        :param field_name:
        :param args: (name, type) tuples
        :param kwargs: parent class kwargs
        """
        items = list()
        for i in xrange(8, 0, -1):
            items.append((field_name + str(i), Bits(maxlen=1, value=0)))
        super(PresenceFlags, self).__init__(*(items+list(args)), **kwargs)
