"""EGTS_SR_LOOPIN_DATA"""
from ....egts_types import *
from . import presence_flags


class LoopinData(EGTSRecord):
    """EGTS_SR_LOOPIN_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(LoopinData, self).__init__(
            # Flags calculated based on fields existance
            ('life_flags', presence_flags.PresenceFlags(field_name='life')),
            # Flags are calculated based on fields existence
            ('lis', ArrayOfType(of_type=Lis, maxlen=4, optional=True)),
            *args, **kwargs
        )

    @property
    def special_inputs(self):
        def generate_setter(number):
            flags = self['life_flags']
            predecessors = 0
            for i in xrange(1, number, 2):
                if flags['life{}'.format(i)].value or flags['life{}'.format(i+1)].value:
                    predecessors += 1

            def setter(value):
                if number % 2:
                    position = 'lis_odd'
                else:
                    position = 'lis_even'
                if flags['life{}'.format(number)] == 0b1:
                    self['lis'][predecessors][position] = value
                else:
                    new_field = Lis()
                    new_field[position] = value
                    self['lis'].insert(predecessors, new_field)
                    flags['life{}'.format(number)] = 0b1

            return setter

        return {'lis{}'.format(num): generate_setter(num) for num in range(1, 9)}


class Lis(BitField):
    """EGTS_SR_LOOPIN_DATA Loop In State (4 bits each)"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Lis, self).__init__(
            # Flags calculated based on fields existance
            ('lis_odd', Bits(maxlen=4, value=0)),
            ('lis_even', Bits(maxlen=4, value=0)),
            *args, **kwargs
        )
