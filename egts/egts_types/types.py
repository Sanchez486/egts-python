"""EGTS Types Classes. All the types are taken from docs."""
import copy
import struct
import abc
import collections
import enum
import binascii


class EGTSField(object):
    """Base EGTS Field class"""
    __metaclass__ = abc.ABCMeta

    def __init__(self,
                 value=None,
                 optional=False,
                 minlen=0, maxlen=None):
        """
        Constructor. Defines basic features of every EGTS field
        :param value: predefined value
        :param optional: flag indicates if field could be skipped
        :param minlen: minimum field length. 0 is default
        :param maxlen: maximum field length
        """
        # initial value format is defined in a parent class
        # None/OrderedDict/list/etc.
        self._optional = optional
        self._minlen = minlen
        self._maxlen = maxlen
        if maxlen and maxlen < minlen:
            raise TypeError('Length error! minlen > maxlen')

        if value is not None:
            self.value = value

    @abc.abstractmethod
    def __len__(self):
        """
        Each field must be able to calculate length in bytes
        :return: length in bytes
        """
        raise NotImplementedError

    @abc.abstractmethod
    def __str__(self):
        """
        Each field must be able to calculate octet string
        :return: octet string
        """
        raise NotImplementedError

    @abc.abstractproperty
    def _input_casts(self):
        """
        Each field type supports different inputs
        :return: inputs dictionary
        """
        raise NotImplementedError

    @property
    def specified(self):
        """
        Field is skipped if it is both optional and empty (/not ready)
        :return: True if cannot be skipped, False if skipped
        """
        raise NotImplementedError

    @property
    def value(self):
        """
        Initial value format is defined in a parent class
        None/OrderedDict/list/etc.
        :return: field value
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Field value setter. Input formats are defined in _input_casts
        :param value: value to set
        """
        # pylint: disable=unidiomatic-typecheck
        if type(value) in self._input_casts:
            cast = self._input_casts[type(value)]
        else:
            raise TypeError('Cannot assign {} to {}'.format(type(value),
                                                            type(self)))
        # pylint: enable=unidiomatic-typecheck
        cast(value)
        self._validate()

    def _size_validate(self):
        """
        Validate if field's size is appropriate
        """
        pass

    def _validate(self):
        """
        Validate if field's value is appropriate
        """
        if self._maxlen:
            self._size_validate()


class Simple(EGTSField):
    """Simple EGTS Field which contains only its own value"""
    __metaclass__ = abc.ABCMeta

    # Redefined if field has constant size
    _SIZE = None

    def __init__(self, *args, **kwargs):
        """
        Simple field constructor
        :param args: parent class args
        :param kwargs: parent class kwargs
        """
        # default value is None for Simple fields
        self._value = None
        super(Simple, self).__init__(*args, **kwargs)
        if not (self._SIZE is None) ^ (self._maxlen is None):
            raise TypeError('Indefinite field size!')

    def __len__(self):
        """
        Length method
        :return: field length in bytes
        """
        if self._maxlen:
            return len(str(self)) // 2
        else:
            # if there is no maxlen, field's constant size is returned
            return self._SIZE

    @property
    def _input_casts(self):
        """
        Input casts for simple fields are simple python types
        :return: (input format: cast function) dict
        """
        return {
            None: self.unset,
            int: self._int_cast,
            str: self._string_cast,
            unicode: self._unicode_cast,
            bool: self._bool_cast,
            enum.Enum: self._enum_cast
        }

    def unset(self, value=None):
        """
        Set simple field back to None
        :param value: None
        """
        if value is not None:
            raise TypeError('Simple field can only be unset to None!')
        self._value = value

    def __str__(self):
        """
        Pack value into little-endian octet string
        :return: little-endian octet string
        """
        return self.bytes.encode('hex')

    @property
    def bytes(self):
        return struct.pack(self._format_char, self._value)

    def _int_cast(self, value):
        """
        Cast int value.
        :param value: int value
        """
        raise NotImplementedError

    def _string_cast(self, value):
        """
        Cast string value.
        :param value: string value
        """
        raise NotImplementedError

    def _unicode_cast(self, value):
        """
        Cast unicode value.
        :param value: unicode value
        """
        self._string_cast(str(value))

    def _bool_cast(self, value):
        """
        Cast boolean value.
        :param value: boolean value
        """
        self._int_cast(int(value))

    def _enum_cast(self, value):
        """
        Cast enum value (when enum member is assigned)
        :param value: enum value
        """
        self.value = value.value

    @abc.abstractproperty
    def _format_char(self):
        """
        Each simple class must have a format char for str packing
        :return: char for "struct" formatting
        """
        raise NotImplementedError

    def _validate(self):
        """
        Validate if field's value is appropriate
        """
        super(Simple, self)._validate()
        str(self)

    def _size_validate(self):
        """
        Validate if field's size is appropriate
        """
        length = len(self)
        if not self._minlen <= length <= self._maxlen:
            raise OverflowError(
                'Wrong length! Got {} instead of {} <= len <= {} '.
                format(length, self._minlen, self._maxlen))

    @property
    def specified(self):
        """
        Field is skipped if it is both optional and empty (/not ready)
        :return: True if cannot be skipped, False if skipped
        """
        return not (self._optional and self._value is None)


class IntStored(Simple):
    """
    Base for field with value stored in int
    """
    __metaclass__ = abc.ABCMeta

    def _string_cast(self, value):
        """
        Cast string value.
        :param value: string value
        """
        if value[0:2] == '0x':
            self._value = int(value, 16)
        elif value[0:2] == '0b':
            self._value = int(value, 2)
        else:
            self._value = int(value)

    def _int_cast(self, value):
        """
        Cast int value.
        :param value: int value
        """
        self._value = value


class LongStored(Simple):
    """
    Base for field with value stored in long
    """
    __metaclass__ = abc.ABCMeta

    @property
    def _input_casts(self):
        """
        Add long cast in input casts
        :return: (input format: cast function) dict
        """
        casts = super(LongStored, self)._input_casts
        casts[long] = self._long_cast
        return casts

    def _string_cast(self, value):
        """
        Cast string value.
        :param value: string value
        """
        if value[0:2] == '0x':
            self._value = long(value, 16)
        elif value[0:2] == '0b':
            self._value = long(value, 2)
        else:
            self._value = long(value)

    def _long_cast(self, value):
        """
        Cast long value.
        :param value: long value
        """
        self._value = value

    def _int_cast(self, value):
        """
        Cast int value.
        :param value: int value
        """
        self._value = long(value)


class FloatStored(Simple):
    """
    Base for field with value stored in float
    """
    __metaclass__ = abc.ABCMeta

    @property
    def _input_casts(self):
        """
        Add float cast in input casts
        :return: (input format: cast function) dict
        """
        casts = super(FloatStored, self)._input_casts
        casts[float] = self._float_cast
        return casts

    def _string_cast(self, value):
        """
        Cast string value.
        :param value: string value
        """
        self._float_cast(float(value))

    def _int_cast(self, value):
        """
        Cast int value.
        :param value: int value
        """
        self._float_cast(float(value))

    def _float_cast(self, value):
        """
        Cast float value.
        :param value: float value
        """
        if 'inf' in str(value):
            raise OverflowError('Float is too large!')
        self._value = value


class String(Simple):
    """String Type Object"""
    def __init__(self, fixed=False, *args, **kwargs):
        self._fixed = fixed
        super(String, self).__init__(*args, **kwargs)

    def __len__(self):
        return len(self._value)

    @property
    def _format_char(self):
        """
        Format char depends on string length
        :return: format char for "struct" formatting
        """
        if self._fixed:
            length = self._maxlen
        else:
            length = len(self)
        return '<{}s'.format(length)

    def _long_cast(self, value):
        """
        Cast long value.
        :param value: long value
        """
        self._string_cast(str(value))

    def _int_cast(self, value):
        """
        Cast int value.
        :param value: int value
        """
        self._string_cast(str(value))

    def _unicode_cast(self, value):
        self._string_cast(value.encode('cp1251'))

    def _string_cast(self, value):
        """
        Cast string value. Encode it to cp-1251 according to EGTS Standard
        :param value: string value
        """
        try:
            self._value = value.decode('utf-8').encode('cp1251')
        except UnicodeDecodeError:
            self._value = value


class Bits(Simple):
    """Bits object"""
    def __str__(self):
        """
        Format char depends on bitfield length
        :return: format char for "struct" formatting
        """
        return '{:0{}b}'.format(self._value, self._maxlen)

    def __len__(self):
        """
        Fixed length for bits
        :return: bits quantity
        """
        return self._maxlen

    def _int_cast(self, value):
        """
        Cast int value.
        :param value: int value
        """
        self._value = value

    def _string_cast(self, value):
        """
        Cast string value.
        :param value: string value
        """
        if value[0:2] == '0x':
            self._value = int(value, 16)
        else:
            self._value = int(value, 2)

    @property
    def _format_char(self):
        """
        Bits do not have any format char because str method is overridden
        """
        return None

    def _size_validate(self):
        """
        Validate if field's size is appropriate
        """
        length = len(str(self))
        if not self._minlen <= length <= self._maxlen:
            raise OverflowError(
                'Wrong length! Got {} instead of {} <= len <= {} '.
                format(length, self._minlen, self._maxlen))


class Boolean(Simple):
    """Boolean Type Object"""
    _SIZE = 1

    @property
    def _format_char(self):
        """
        Boolean format char
        :return: format char for "struct" formatting
        """
        return '<?'

    def _string_cast(self, value):
        """
        Cast string value.
        :param value: string value
        """
        val = value.lower()
        if val == 'true':
            self._value = True
        elif val == 'false':
            self._value = False
        elif val == '1':
            self._value = True
        elif val == '0':
            self._value = False
        else:
            raise TypeError('Cannot assign "{}" str to Boolean'.format(value))

    def _int_cast(self, value):
        """
        Cast int value.
        :param value: int value
        """
        if value == 1:
            self._value = True
        elif value == 0:
            self._value = False
        else:
            raise TypeError('Cannot assign {} to Boolean'.format(value))


class Byte(IntStored):
    """Byte Type"""
    # Byte has fixed size of 1
    _SIZE = 1

    @property
    def _format_char(self):
        """
        Byte format char
        :return: format char for "struct" formatting
        """
        return '<B'


class UShort(IntStored):
    """UShort Type"""
    # Ushort has fixed size of 1
    _SIZE = 2

    @property
    def _format_char(self):
        """Encoded as unsigned short"""
        return '<H'


class UInt(IntStored):
    """UInt Type"""
    # UInt has fixed size of 4
    _SIZE = 4

    @property
    def _format_char(self):
        """Encoded as unsigned int"""
        return '<I'


class ULong(LongStored):
    """ULong Type"""
    # ULong has fixed size of 8
    _SIZE = 8

    @property
    def _format_char(self):
        return '<Q'


class Short(IntStored):
    """Short Type"""
    # Short has fixed size of 2
    _SIZE = 2

    @property
    def _format_char(self):
        """Encoded as signed short"""
        return '<h'


class Int(IntStored):
    """Int Type"""
    # Int has fixed size of 4
    _SIZE = 4

    @property
    def _format_char(self):
        """Encoded as signed int"""
        return '<i'


class Float(FloatStored):
    """Float Type"""
    # Float has fixed size of 4
    _SIZE = 4

    @property
    def _format_char(self):
        return '<f'


class Double(FloatStored):
    """Double Type"""
    # Double has fixed size of 8
    _SIZE = 8

    @property
    def _format_char(self):
        return '<d'


class Compound(EGTSField):
    """Base class for fields containing more fields inside"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def fields(self):
        """
        Field values generator
        :return: field values without names
        """
        raise NotImplementedError

    def __str__(self):
        """
        Calculate octet string
        :return: octet string
        """
        return binascii.hexlify(self.bytes)

    def is_ready(self):
        """
        Check all the fields are set and field is ready to be calculated
        :return: True/False
        """
        raise NotImplementedError

    def __len__(self):
        """
        Length method
        :return: field length in bytes
        """
        length = 0
        for field in self.fields:
            if field.specified:
                length += len(field)
        return length

    @property
    def bytes(self):
        """
        Calculate byte array for the field
        :return: byte values (0 <= x <= 255) tuple
        """
        if self.is_ready():
            byte_string = b''
            for field in self.fields:
                if field.specified:
                    byte_string += field.bytes
            return byte_string
        else:
            # Cannot calculate string unless all the required fields are set
            raise KeyError('Some required fields were not set!')

    @property
    def specified(self):
        """
        Field is skipped if it is both optional and not ready
        :return: True if cannot be skipped, False if skipped
        """
        return not self._optional or self.is_ready()

    @abc.abstractmethod
    def __getitem__(self, item):
        """
        Compound field must support item assignment
        :param item: field's key (name/number)
        :return: field
        """
        raise NotImplementedError

    @abc.abstractmethod
    def __setitem__(self, key, value):
        """
        Compound field must support item assignment
        :param key: field's key (name/number)
        :param value: value to set
        """
        raise NotImplementedError


class EGTSRecord(Compound):
    """EGTS Record with (name: field) dict"""
    def __init__(self, *args, **kwargs):
        """
        EGTSRecord field constructor
        :param args: (name, type) tuples
        :param kwargs: parent class kwargs
        """
        # default value is OrderedDict with fields for Simple fields
        self._value = collections.OrderedDict(args)
        super(EGTSRecord, self).__init__(**kwargs)

    @property
    def fields(self):
        """
        Field values generator
        :return: field values without names
        """
        for field in self._value.values():
            yield field

    def is_ready(self):
        """
        Check all the fields are set and field is ready to be calculated
        :return: True/False
        """
        self.prepare()
        for field in self.fields:
            if field.specified:
                if isinstance(field, Compound):
                    if not field.is_ready():
                        return False
                elif isinstance(field, Simple):
                    if field.value is None:
                        return False
        return True

    def prepare(self):
        """
        Set counted data (lengths and checksums) from bottom to the top
        """
        for field in self.fields:
            if isinstance(field, Compound):
                field.prepare()
        self.set_fields()

    def set_fields(self):
        """
        Override this method to calculate necessary fields
        """
        pass

    @property
    def _input_casts(self):
        """
        Input cast for simple fields is values dict
        :return: (input format: cast function) dict
        """
        return {
            dict: self._dict_cast
        }

    def _dict_cast(self, value):
        """
        Assign values using a dict.
        DOES NOT SUPPORT ENCLOSED FIELD SETTING
        :param value: values dictionary
        """
        for field in value.keys():
            self[field] = value[field]

    @property
    def special_inputs(self):
        return {}

    def __getitem__(self, item):
        """
        Get field by its name (supports enclosing)
        :param item: field's name
        :return: field object
        """
        if item in self._value.keys():
            field = self._value[item]
            if field is None:
                raise KeyError('{} type was not set!'.format(item))
            else:
                return self._value[item]
        else:
            for field in self.fields:
                if isinstance(field, EGTSRecord):
                    try:
                        return field[item]
                    except KeyError:
                        pass
                if isinstance(field, ArrayOfType):
                    if isinstance(item, int):
                        return field[item]
                    for i in xrange(0, field.quantity):
                        try:
                            return field[i][item]
                        except (KeyError, IndexError):
                            pass
            raise KeyError('{} field not found!'.
                           format(item))

    def __setitem__(self, key, value):
        """
        Set field by its name (supports enclosing)
        :param key: field's name
        :param value: value to set
        """
        if key in self.special_inputs:
            self.special_inputs[key](value)
        else:
            if isinstance(value, EGTSField):
                self._value[key] = copy.deepcopy(value)
            else:
                self[key].value = value


class BitField(EGTSRecord):
    """Bit Field class"""
    def __init__(self, *args, **kwargs):
        """
        Bit Field constructor
        :param args: (name, type) tuples
        :param kwargs: parent class kwargs
        """
        super(BitField, self).__init__(*args, **kwargs)
        length = 0
        for field in self.fields:
            if not isinstance(field, Bits):
                raise TypeError(
                    'BitField contains only Bits!')
            length += len(field)
        if length % 8 != 0:
            raise TypeError('Number of bits must be a multiple of 8!')

    def __len__(self):
        """Length in bytes = Length in bits/8"""
        return super(BitField, self).__len__() // 8

    @property
    def bitstring(self):
        if self.is_ready():
            bit_string = ''
            for field in self.fields:
                bit_string += str(field)
            return bit_string
        else:
            raise KeyError('Some required fields were not set!')

    def __str__(self):
        """
        str method overriding
        :return: octet string (bytes)
        """
        bit_string = self.bitstring
        string = ''
        for i in xrange(0, len(bit_string), 8):
            # MAY BE WRONG BYTES ORDER
            string += '{:02x}'.format(int(bit_string[i:i+8], 2))
        return string

    @property
    def bytes(self):
        return binascii.unhexlify(str(self))


class ArrayOfType(Compound):
    """Array of specified fields"""
    def __init__(self, of_type, *args, **kwargs):
        """
        Array of type field constructor
        :param of_type: type of members
        :param args: parent class args
        :param kwargs: parent class kwargs
        """
        self._value = list()
        self._type = of_type
        super(ArrayOfType, self).__init__(*args, **kwargs)

    @property
    def quantity(self):
        """
        Array size
        :return: array size
        """
        return len(self._value)

    @property
    def fields(self):
        """
        Field values generator
        :return: field values without names
        """
        for field in self._value:
            yield field

    def is_ready(self):
        """
        Check all the fields are set and field is ready to be calculated
        :return: True/False
        """
        self.prepare()
        for field in self.fields:
            if field.specified:
                if isinstance(field, Compound):
                    if not field.is_ready():
                        return False
                elif isinstance(field, Simple):
                    if field.value is None:
                        return False
        return True

    def prepare(self):
        """
        Set counted data (lengths and checksums) from bottom to the top
        """
        if issubclass(self._type, Compound):
            for field in self.fields:
                field.prepare()

    @property
    def _input_casts(self):
        """
        Input casts for Array of type are list, tuple or hex string
        :return: (input format: cast function) dict
        """
        return {
            list: self._list_cast,
            tuple: self._tuple_cast,
            str: self._string_cast,
            unicode: self._unicode_cast
        }

    def _tuple_cast(self, value):
        """
        Assign values using a dict.
        DOES NOT SUPPORT ENCLOSED FIELD SETTING
        :param value: values dictionary
        """
        for i in xrange(0, len(value)):
            self[i] = value[i]

    def _list_cast(self, value):
        """
        Cast list value.
        :param value: list value
        """
        self._tuple_cast(value)

    def _string_cast(self, value):
        """
        Cast string value.
        :param value: string value
        """
        if issubclass(self._type, Simple):
            if value[0:2] == '0x':
                size = len(self._type()) * 2
                index = 0
                for i in xrange(2, len(value), size):
                    self[index] = '0x' + value[i:i+size]
                    index += 1
            else:
                raise TypeError('Need byte string to assign str to array!')
        else:
            raise TypeError('Cannot assign str to {}'.format(type(self)))

    def _unicode_cast(self, value):
        """
        Cast unicode value.
        :param value: unicode value
        """
        self._string_cast(str(value))

    def __getitem__(self, item):
        """
        Get field by its number
        :param item: field's number
        :return: field object
        """
        return self._value[item]

    def __setitem__(self, key, value):
        """
        Set field by its number
        :param key: field's number
        :param value: value to set
        """
        if key == self.quantity:
            self.append(value)
        else:
            self[key].value = value

    def append(self, value=None):
        """
        Add new item to array
        :param value: value to add
        """
        if isinstance(value, EGTSField):
            if isinstance(value, self._type):
                self._value.append(copy.deepcopy(value))
            else:
                raise TypeError('Cannot append {} to array of {}'
                                .format(type(value), self._type))
        else:
            self._value.append(self._type(value=value))
        self._validate()

    def _size_validate(self):
        """
        Validate if array's size is appropriate
        """
        length = self.quantity
        if not self._minlen <= length <= self._maxlen:
            raise OverflowError(
                'Cannot add another element to the array (maxlen=={})'.
                format(self._maxlen))
