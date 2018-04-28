"""EGTS types testing"""
import pytest
import struct


class TestByte:
    @pytest.fixture(scope='class')
    def field(self, value=None):
        """Init test field"""
        from egts.egts_types.types import Byte
        return Byte(value)

    @pytest.mark.parametrize("test_input,expected", [
        (100, 100),
        ("200", 200),
        (u"150", 150),
        (True, 1)
    ])
    def test_value_assignment(self, test_input, expected):
        """Test Value Assignment"""
        field = self.field()
        field.value = test_input
        assert field.value == expected

    @pytest.mark.parametrize("test_input,expected", [
        (-1, struct.error),
        (256, struct.error)
    ])
    def test_value_assignment_failed(self, test_input, expected):
        """Test incorrect value assignment"""
        field = self.field()
        with pytest.raises(expected):
            field.value = test_input

    @pytest.mark.parametrize("test_input,expected", [
        (10, b'\x0a')
    ])
    def test_bytes(self, test_input, expected):
        """Test bytes conversion"""
        field = self.field()
        field.value = test_input
        assert field.bytes == expected

    @pytest.mark.parametrize("test_input,expected", [
        (255, 'ff')
    ])
    def test_str(self, test_input, expected):
        """Test string conversion"""
        field = self.field()
        field.value = test_input
        assert str(field) == expected

    def test_len(self):
        """Test length calculation"""
        assert len(self.field()) == 1


class TestUShort:
    @pytest.fixture(scope='class')
    def field(self, value=None):
        """Init test field"""
        from egts.egts_types.types import UShort
        return UShort(value)

    @pytest.mark.parametrize("test_input,expected", [
        (-1, struct.error),
        (65536, struct.error)
    ])
    def test_value_assignment_failed(self, test_input, expected):
        """Test incorrect value assignment"""
        field = self.field()
        with pytest.raises(expected):
            field.value = test_input

    @pytest.mark.parametrize("test_input,expected", [
        (100, 100),
        ("200", 200),
        (u"150", 150),
        (True, 1)
    ])
    def test_value_assignment(self, test_input, expected):
        """Test Value Assignment"""
        field = self.field()
        field.value = test_input
        assert field.value == expected

    @pytest.mark.parametrize("test_input,expected", [
        (0x0afe, 'fe0a')
    ])
    def test_str(self, test_input, expected):
        """Test string conversion"""
        field = self.field()
        field.value = test_input
        assert str(field) == expected

    @pytest.mark.parametrize("test_input,expected", [
        (10, b'\x0a\x00')
    ])
    def test_bytes(self, test_input, expected):
        """Test bytes conversion"""
        field = self.field()
        field.value = test_input
        assert field.bytes == expected

    def test_len(self):
        """Test length calculation"""
        assert len(self.field()) == 2


class TestUInt:
    @pytest.fixture(scope='class')
    def field(self, value=None):
        """Init test field"""
        from egts.egts_types.types import UInt
        return UInt(value)

    @pytest.mark.parametrize("test_input,expected", [
        (-1, struct.error),
        (4294967296, TypeError)
    ])
    def test_value_assignment_failed(self, test_input, expected):
        """Test incorrect value assignment"""
        field = self.field()
        with pytest.raises(expected):
            field.value = test_input

    @pytest.mark.parametrize("test_input,expected", [
        (100, 100),
        ("200", 200),
        (u"150", 150),
        (True, 1)
    ])
    def test_value_assignment(self, test_input, expected):
        """Test Value Assignment"""
        field = self.field()
        field.value = test_input
        assert field.value == expected
    
    @pytest.mark.parametrize("test_input,expected", [
        (100, 100),
        ("200", 200),
        (u"150", 150),
        (True, 1)
    ])
    def test_value_assignment(self, test_input, expected):
        """Test Value Assignment"""
        field = self.field()
        field.value = test_input
        assert field.value == expected

    def test_len(self):
        """Test length calculation"""
        assert len(self.field()) == 4
    
    @pytest.mark.parametrize("test_input,expected", [
        (0x0afe0011, '1100fe0a')
    ])
    def test_str(self, test_input, expected):
        """Test string conversion"""
        field = self.field()
        field.value = test_input
        assert str(field) == expected

    @pytest.mark.parametrize("test_input,expected", [
        (10, b'\x0a\x00\x00\x00')
    ])
    def test_bytes(self, test_input, expected):
        """Test bytes conversion"""
        field = self.field()
        field.value = test_input
        assert field.bytes == expected


class TestULong:
    from sys import maxint
    LONG_VALUE = maxint + 1

    @pytest.fixture(scope='class')
    def field(self, value=None):
        """Init test field"""
        from egts.egts_types.types import ULong
        return ULong(value)

    @pytest.mark.parametrize("test_input,expected", [
        (-1, struct.error),
        (18446744073709551616, struct.error)
    ])
    def test_value_assignment_failed(self, test_input, expected):
        """Test incorrect value assignment"""
        field = self.field()
        with pytest.raises(expected):
            field.value = test_input

    @pytest.mark.parametrize("test_input,expected", [
        (100, 100),
        (LONG_VALUE, LONG_VALUE),
        ("200", 200),
        (u"150", 150),
        (True, 1)
    ])
    def test_value_assignment(self, test_input, expected):
        """Test Value Assignment"""
        field = self.field()
        field.value = test_input
        assert field.value == expected
        assert type(field.value) is long

    def test_len(self):
        """Test length calculation"""
        assert len(self.field()) == 8
    
    @pytest.mark.parametrize("test_input,expected", [
        (0x0afe00110bfe0011, '1100fe0b1100fe0a')
    ])
    def test_str(self, test_input, expected):
        """Test string conversion"""
        field = self.field()
        field.value = test_input
        assert str(field) == expected

    @pytest.mark.parametrize("test_input,expected", [
        (10, b'\x0a\x00\x00\x00\x00\x00\x00\x00')
    ])
    def test_bytes(self, test_input, expected):
        """Test bytes conversion"""
        field = self.field()
        field.value = test_input
        assert field.bytes == expected


class TestShort:
    @pytest.fixture(scope='class')
    def field(self, value=None):
        """Init test field"""
        from egts.egts_types.types import Short
        return Short(value)

    @pytest.mark.parametrize("test_input,expected", [
        (-32769, struct.error),
        (32768, struct.error)
    ])
    def test_value_assignment_failed(self, test_input, expected):
        """Test incorrect value assignment"""
        field = self.field()
        with pytest.raises(expected):
            field.value = test_input

    @pytest.mark.parametrize("test_input,expected", [
        (100, 100),
        ("-200", -200),
        (u"150", 150),
        (True, 1)
    ])
    def test_value_assignment(self, test_input, expected):
        """Test Value Assignment"""
        field = self.field()
        field.value = test_input
        assert field.value == expected

    def test_len(self):
        """Test length calculation"""
        assert len(self.field()) == 2
    
    @pytest.mark.parametrize("test_input,expected", [
        (-10000, 'f0d8')
    ])
    def test_str(self, test_input, expected):
        """Test string conversion"""
        field = self.field()
        field.value = test_input
        assert str(field) == expected

    @pytest.mark.parametrize("test_input,expected", [
        (-10000, 'f0d8')
    ])
    def test_str(self, test_input, expected):
        """Test string conversion"""
        field = self.field()
        field.value = test_input
        assert str(field) == expected

    @pytest.mark.parametrize("test_input,expected", [
        (-10, b'\xf6\xff')
    ])
    def test_bytes(self, test_input, expected):
        """Test bytes conversion"""
        field = self.field()
        field.value = test_input
        assert field.bytes == expected


class TestInt:
    @pytest.fixture(scope='class')
    def field(self, value=None):
        """Init test field"""
        from egts.egts_types.types import Int
        return Int(value)

    @pytest.mark.parametrize("test_input,expected", [
        (-2147483649, TypeError),
        (2147483648, TypeError)
    ])
    def test_value_assignment_failed(self, test_input, expected):
        """Test incorrect value assignment"""
        field = self.field()
        with pytest.raises(expected):
            field.value = test_input

    @pytest.mark.parametrize("test_input,expected", [
        (100, 100),
        ("-200", -200),
        (u"150", 150),
        (True, 1)
    ])
    def test_value_assignment(self, test_input, expected):
        """Test Value Assignment"""
        field = self.field()
        field.value = test_input
        assert field.value == expected
    
    @pytest.mark.parametrize("test_input,expected", [
        (-70000, '90eefeff')
    ])
    def test_str(self, test_input, expected):
        """Test string conversion"""
        field = self.field()
        field.value = test_input
        assert str(field) == expected

    def test_len(self):
        """Test length calculation"""
        assert len(self.field()) == 4

    @pytest.mark.parametrize("test_input,expected", [
        (-10, b'\xf6\xff\xff\xff')
    ])
    def test_bytes(self, test_input, expected):
        """Test bytes conversion"""
        field = self.field()
        field.value = test_input
        assert field.bytes == expected


class TestFloat:
    @pytest.fixture(scope='class')
    def field(self, value=None):
        """Init test field"""
        from egts.egts_types.types import Float
        return Float(value)

    @pytest.mark.parametrize("test_input,expected", [
        (-3.4e+39, OverflowError),
        (3.4e+39, OverflowError)
    ])
    def test_value_assignment_failed(self, test_input, expected):
        """Test incorrect value assignment"""
        field = self.field()
        with pytest.raises(expected):
            field.value = test_input

    @pytest.mark.parametrize("test_input,expected", [
        (100, 100),
        ('-200.5', -200.5),
        (u"150", 150),
        (True, 1.0),
        (265.42, 265.42)
    ])
    def test_value_assignment(self, test_input, expected):
        """Test Value Assignment"""
        field = self.field()
        field.value = test_input
        assert field.value == expected
        assert type(field.value) is float

    @pytest.mark.parametrize("test_input,expected", [
        (-265.42, 'c3b584c3')
    ])
    def test_str(self, test_input, expected):
        """Test string conversion"""
        field = self.field()
        field.value = test_input
        assert str(field) == expected

    @pytest.mark.parametrize("test_input,expected", [
        (-3.14, b'\xc3\xf5\x48\xc0')
    ])
    def test_bytes(self, test_input, expected):
        """Test bytes conversion"""
        field = self.field()
        field.value = test_input
        assert field.bytes == expected

    def test_len(self):
        """Test length calculation"""
        assert len(self.field()) == 4


class TestDouble:
    @pytest.fixture(scope='class')
    def field(self, value=None):
        """Init test field"""
        from egts.egts_types.types import Double
        return Double(value)

    @pytest.mark.parametrize("test_input,expected", [
        (-1.7e+309, OverflowError),
        (1.7e+309, OverflowError)
    ])
    def test_value_assignment_failed(self, test_input, expected):
        """Test incorrect value assignment"""
        field = self.field()
        with pytest.raises(expected):
            field.value = test_input

    @pytest.mark.parametrize("test_input,expected", [
        (100, 100),
        (3.4e+39, 3.4e+39),
        ('-200.5', -200.5),
        (u"150", 150),
        (True, 1.0),
        (265.42, 265.42)
    ])
    def test_value_assignment(self, test_input, expected):
        """Test Value Assignment"""
        field = self.field()
        field.value = test_input
        assert field.value == expected
        assert type(field.value) is float

    @pytest.mark.parametrize("test_input,expected", [
        (-3.14, b'\x1f\x85\xeb\x51\xb8\x1e\x09\xc0')
    ])
    def test_bytes(self, test_input, expected):
        """Test bytes conversion"""
        field = self.field()
        field.value = test_input
        assert field.bytes == expected

    @pytest.mark.parametrize("test_input,expected", [
        (-3.4e+39, 'cc0bb85cc0fb23c8')
    ])
    def test_str(self, test_input, expected):
        """Test string conversion"""
        field = self.field()
        field.value = test_input
        assert str(field) == expected

    def test_len(self):
        """Test length calculation"""
        assert len(self.field()) == 8


class TestBoolean:
    @pytest.fixture(scope='class')
    def field(self, value=None):
        """Init test field"""
        from egts.egts_types.types import Boolean
        return Boolean(value)

    @pytest.mark.parametrize("test_input,expected", [
        (2, TypeError),
        (-1, TypeError)
    ])
    def test_value_assignment_failed(self, test_input, expected):
        """Test incorrect value assignment"""
        field = self.field()
        with pytest.raises(expected):
            field.value = test_input

    @pytest.mark.parametrize("test_input,expected", [
        (1, True),
        ('False', False),
        (u'True', True),
        (True, True)
    ])
    def test_value_assignment(self, test_input, expected):
        """Test Value Assignment"""
        field = self.field()
        field.value = test_input
        assert field.value is expected

    @pytest.mark.parametrize("test_input,expected", [
        (0, b'\x00')
    ])
    def test_bytes(self, test_input, expected):
        """Test bytes conversion"""
        field = self.field()
        field.value = test_input
        assert field.bytes == expected

    @pytest.mark.parametrize("test_input,expected", [
        (True, '01')
    ])
    def test_str(self, test_input, expected):
        """Test string conversion"""
        field = self.field(test_input)
        assert str(field) == expected

    def test_len(self):
        """Test length calculation"""
        assert len(self.field()) == 1


class TestString:
    from sys import maxint
    LONG_VALUE = maxint + 1

    @pytest.fixture(scope='class')
    def field(self, value=None, *args, **kwargs):
        """Init test field"""
        from egts.egts_types.types import String
        return String(value, *args, **kwargs)

    @pytest.mark.parametrize("minlen,maxlen,test_input,expected", [
        (2, 3, 'a', OverflowError),
        (2, 3, 'abcd', OverflowError)
    ])
    def test_value_assignment_failed(self, minlen, maxlen, test_input, expected):
        """Test incorrect value assignment"""
        field = self.field(minlen=minlen, maxlen=maxlen)
        with pytest.raises(expected):
            field.value = test_input

    @pytest.mark.parametrize("test_input,expected", [
        (100, '100'),
        ('1a2b', '1a2b'),
        (u'a1b2', 'a1b2'),
        (True, '1')
    ])
    def test_value_assignment(self, test_input, expected):
        """Test Value Assignment"""
        field = self.field(maxlen=5)
        field.value = test_input
        assert field.value == expected

    @pytest.mark.parametrize("test_input,expected", [
        ('c3d4', b'\x63\x33\x64\x34')
    ])
    def test_bytes(self, test_input, expected):
        """Test string conversion"""
        field = self.field(maxlen=4)
        field.value = test_input
        assert field.bytes == expected

    @pytest.mark.parametrize("test_input,expected", [
        ('a1b2', '61316232')
    ])
    def test_str(self, test_input, expected):
        """Test string conversion"""
        field = self.field(maxlen=10)
        field.value = test_input
        assert str(field) == expected

    @pytest.mark.parametrize("test_input,expected", [
        ('A2345', 5)
    ])
    def test_len(self, test_input, expected):
        """Test length calculation"""
        field = self.field(maxlen=100)
        field.value = test_input
        assert len(field) == expected


class TestBits:
    @pytest.fixture(scope='class')
    def field(self, value=None, *args, **kwargs):
        """Init test field"""
        from egts.egts_types.types import Bits
        return Bits(value, *args, **kwargs)

    @pytest.mark.parametrize("minlen,maxlen,test_input,expected", [
        (3, 0b1101, OverflowError),
        (3, -1, TypeError)
    ])
    def test_value_assignment_failed(self, maxlen, test_input, expected):
        """Test incorrect value assignment"""
        field = self.field(maxlen=maxlen)
        with pytest.raises(expected):
            field.value = test_input

    @pytest.mark.parametrize("test_input,expected", [
        (0b100, 4),
        ('0b010', 2),
        (u'0b110', 6),
        (True, 1)
    ])
    def test_value_assignment(self, test_input, expected):
        """Test Value Assignment"""
        field = self.field(maxlen=5)
        field.value = test_input
        assert field.value == expected

    @pytest.mark.parametrize("test_input,expected", [
        (0b0110, '00110')
    ])
    def test_str(self, test_input, expected):
        """Test string conversion"""
        field = self.field(maxlen=5)
        field.value = test_input
        assert str(field) == expected

    @pytest.mark.parametrize("test_input,expected", [
        (5, 5)
    ])
    def test_len(self, test_input, expected):
        """Test length calculation"""
        field = self.field(maxlen=test_input)
        field.value = 1
        assert len(field) == expected


class TestEGTSRecord:
    @pytest.fixture(scope='class')
    def field(self, *args, **kwargs):
        """Init test field"""
        from egts.egts_types import EGTSRecord, Byte
        return EGTSRecord(
            ("first", Byte()),
            ("second", EGTSRecord(
                ("third", Byte()),
                ("fourth", Byte()),
            )),
            ("fifth", Byte()),
            *args, **kwargs
        )

    def test_dict(self):
        """Test dict value assignment"""
        field = self.field()
        field.value = {"first": 10,
                       "second": {
                           "third": 30,
                           "fourth": 40
                       },
                       "fifth": 50
                       }
        assert str(field) == '0a1e2832'

    #def test_assignment(self):
    #    field = self.field()
     #   field['first'] =

