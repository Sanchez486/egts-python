"""EGTS_SR_COUNTERS_DATA"""
from ....egts_types import *
from . import presence_flags


class CountersData(EGTSRecord):
    """EGTS_SR_COUNTERS_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(CountersData, self).__init__(
            # Flags calculated based on fields existance
            ('cfe_flags', presence_flags.PresenceFlags(field_name='cfe')),
            # counter fields set outside
            ('cn', ArrayOfType(of_type=Cn, maxlen=8, optional=True)),
            *args, **kwargs
        )

    @property
    def special_inputs(self):
        def generate_setter(number):
            flags = self['cfe_flags']
            predecessors = 0
            for i in xrange(1, number):
                predecessors += flags['cfe{}'.format(i)].value

            def setter(value):
                if flags['cfe{}'.format(number)] == 0b1:
                    self['cn'][predecessors] = value
                else:
                    self['cn'].insert(predecessors, value)
                    flags['cfe{}'.format(number)] = 0b1

            return setter

        return {'cn{}'.format(num): generate_setter(num) for num in range(1, 9)}


class Cn(ArrayOfType):
    """EGTS_SR_COUNTERS_DATA Counter Class"""
    def __init__(self, *args, **kwargs):
        """
        Field of 3 bytes constructor
        """
        super(Cn, self).__init__(of_type=Byte, maxlen=3, minlen=3, *args, **kwargs)
