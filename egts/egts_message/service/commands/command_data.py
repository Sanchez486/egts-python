"""EGTS_SR_COMMAND_DATA"""
from ....egts_types import *


class CommandData(EGTSRecord):
    """EGTS_SR_COMMAND_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(CommandData, self).__init__(
            # Types are set outside
            ('type_flags', TypeFlags()),
            # Command ID. Set Outside
            ('cid', UInt()),
            # Source ID. Set Outside
            ('sid', UInt()),
            # Flags calculated based on fields existence
            ('flags', Flags()),
            # All the following fields are unspecified by default
            ('chs', Byte(optional=True)),
            ('acl', Byte(optional=True)),
            ('ac', ArrayOfType(of_type=Byte, maxlen=255, optional=True)),
            ('cd', CommandDataField()),
            *args, **kwargs
        )

    def set_fields(self):
        """
        Calculate necessary fields
        """
        flags = self['flags']
        flags['acfe'] = int(self['ac'].specified)
        flags['chsfe'] = int(self['chs'].specified)

        if self['ac'].specified:
            self['acl'] = len(self['ac'])

        cmd = self['type_flags']['ct'].value
        mismatch = ((cmd == 0b0001 or cmd == 0b0010 or cmd == 0b1000)
                    == self['cd']['flags'].specified)
        if mismatch:
            raise TypeError('COM/COMCONF mismatch!')


class TypeFlags(BitField):
    """EGTS_SR_COMMAND_DATA Command Type Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(TypeFlags, self).__init__(
            # Types are set outside
            ('ct', Bits(maxlen=4)),
            ('cct', Bits(maxlen=4)),
            *args, **kwargs
        )


class Flags(BitField):
    """EGTS_SR_COMMAND_DATA Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(Flags, self).__init__(
            # Flags calculated based on fields existence
            ('empty', Bits(value=0, maxlen=6)),
            ('acfe', Bits(maxlen=1)),
            ('chsfe', Bits(maxlen=1)),
            *args, **kwargs
        )


class CommandDataField(EGTSRecord):
    """EGTS_SR_COMMAND_DATA Data Field"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(CommandDataField, self).__init__(
            # Command Data info is set outside
            ('adr', UShort()),
            ('flags', FieldFlags(optional=True)),
            ('ccd', UShort()),
            ('dt', ArrayOfType(of_type=Byte, maxlen=65200)),
            *args, **kwargs
        )


class FieldFlags(BitField):
    """EGTS Command Flags"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(FieldFlags, self).__init__(
            # Command Data Flags are set outside
            ('sz', Bits(maxlen=4)),
            ('act', Bits(maxlen=4)),
            *args, **kwargs
        )
