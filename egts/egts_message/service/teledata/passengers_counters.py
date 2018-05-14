"""EGTS_SR_PASSENGERS_COUNTERS"""
from ....egts_types import *
from . import presence_flags


class PassengersCounters(EGTSRecord):
    """EGTS_SR_PASSENGERS_COUNTERS Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(PassengersCounters, self).__init__(
            ('flags', Flags()),
            # All set outside
            ('dpr', presence_flags.PresenceFlags(field_name='dpr')),
            ('drl', Byte()),
            ('maddr', UShort()),
            ('pcd', ArrayOfType(of_type=Pcd, maxlen=8)),
            *args, **kwargs
        )

    @property
    def special_inputs(self):
        flags = self['dpr']

        def get_pcd(number):
            predecessors = 0
            for i in xrange(1, number):
                predecessors += flags['dpr{}'.format(i)].value

            if not flags['dpr{}'.format(number)].value:
                flags['dpr{}'.format(number)] = 0b1
                self['pcd'].insert(predecessors, [None, None])
            return self['pcd'][predecessors]

        def pcd_setter(value):
            for field in value.keys():
                self[field] = value[field]

        def generate_ipq_setter(number):
            def setter(value):
                pcd = get_pcd(number)
                pcd.value = (value, None)

            return setter

        def generate_opq_setter(number):
            def setter(value):
                pcd = get_pcd(number)
                pcd.value = (None, value)

            return setter

        setters = {'pcd': pcd_setter}
        setters.update({'ipq{}'.format(num): generate_ipq_setter(num) for num in range(1, 9)})
        setters.update({'opq{}'.format(num): generate_opq_setter(num) for num in range(1, 9)})
        return setters


class Flags(BitField):
    """EGTS_SR_PASSENGERS_COUNTERS Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Flags, self).__init__(
            ('empty', Bits(maxlen=7, value=0)),
            # Raw data flag zero by default
            ('rdf', Bits(maxlen=1, value=0)),
            *args, **kwargs
        )


class Pcd(ArrayOfType):
    """EGTS_SR_PASSENGERS_COUNTERS Passenger Counters Data"""
    def __init__(self, *args, **kwargs):
        super(Pcd, self).__init__(of_type=Byte, maxlen=2, minlen=2, *args, **kwargs)
