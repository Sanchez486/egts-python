"""Unique Teledata Structure - Array of 8 flags for 8 objects"""
from ....egts_types import *


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
            items.append((field_name + str(i), Bits(1)))
        super(PresenceFlags, self).__init__(*(items+list(args)), **kwargs)
