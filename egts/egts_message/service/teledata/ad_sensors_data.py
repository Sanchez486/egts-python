"""EGTS_SR_AD_SENSORS_DATA"""
from ....egts_types import *
from . import presence_flags


class AdSensorsData(EGTSRecord):
    """EGTS_SR_AD_SENSORS_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(AdSensorsData, self).__init__(
            # Flags calculated based on fields existance
            ('dioe_flags', presence_flags.PresenceFlags(field_name='dioe')),
            # DOUT - set outside?
            ('dout', Byte()),
            # ASFE Flags set outside
            ('asfe_flags', presence_flags.PresenceFlags(field_name='asfe')),
            # digital inputs fields set outside
            ('adio', ArrayOfType(of_type=Byte, maxlen=8, optional=True)),
            # analog sensor fields set outside
            ('ans', ArrayOfType(of_type=Ans, maxlen=8, optional=True)),
            *args, **kwargs
        )

    @property
    def special_inputs(self):
        def generate_adio_setter(number):
            flags = self['dioe_flags']
            predecessors = 0
            for i in xrange(1, number):
                predecessors += flags['dioe{}'.format(i)].value

            def setter(value):
                if flags['dioe{}'.format(number)] == 0b1:
                    self['adio'][predecessors] = value
                else:
                    self['adio'].insert(predecessors, value)
                    flags['dioe{}'.format(number)] = 0b1

            return setter

        def generate_ans_setter(number):
            flags = self['asfe_flags']
            predecessors = 0
            for i in xrange(1, number):
                predecessors += flags['asfe{}'.format(i)].value

            def setter(value):
                if flags['asfe{}'.format(number)] == 0b1:
                    self['ans'][predecessors] = value
                else:
                    self['ans'].insert(predecessors, value)
                    flags['asfe{}'.format(number)] = 0b1
            return setter

        setters = {'adio{}'.format(num): generate_adio_setter(num) for num in range(1, 9)}
        setters.update({'ans{}'.format(num): generate_ans_setter(num) for num in range(1, 9)})
        return setters


class Ans(ArrayOfType):
    """EGTS_SR_AD_SENSORS_DATA Additional Digital Input Class"""
    def __init__(self, *args, **kwargs):
        """
        Field of 3 bytes constructor
        """
        super(Ans, self).__init__(of_type=Byte, maxlen=3, minlen=3,  *args, **kwargs)
