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

    @pytest.mark.parametrize("maxlen,test_input,expected", [
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
        """Init empty test field"""
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

    @pytest.mark.parametrize("first,third,fourth,fifth,expected", [
        (10, 30, 40, 50, '0a1e2832'),
        (0xff, 0x0a, 0xcc, 0x00, 'ff0acc00')
    ])
    def test_str(self, first, third, fourth, fifth, expected):
        """Test field string request"""
        field = self.field()
        test_input = {"first": first,
                      "second": {
                           "third": third,
                           "fourth": fourth
                      },
                      "fifth": fifth
                      }
        field.value = test_input
        assert str(field) == expected

    @pytest.mark.parametrize("first,third,fourth,fifth,expected", [
        (-1, 30, 40, 50, struct.error),
        (0xff, 0x0a, 0xcc, None, ValueError)
    ])
    def test_str_failed(self, first, third, fourth, fifth, expected):
        """Test failed string request"""
        field = self.field()
        test_input = {"first": first,
                      "second": {
                          "third": third,
                          "fourth": fourth
                      },
                      "fifth": fifth
                      }
        with pytest.raises(expected):
            field.value = test_input
            _ = str(field)

    @pytest.mark.parametrize("first,third,fourth,fifth,expected", [
        (10, 30, 40, 50, b'\x0a\x1e\x28\x32'),
        (0xff, 0x0a, 0xcc, 0x00, b'\xff\x0a\xcc\x00')
    ])
    def test_bytes(self, first, third, fourth, fifth, expected):
        """Test field bytes request assignment"""
        field = self.field()
        test_input = {"first": first,
                      "second": {
                          "third": third,
                          "fourth": fourth
                      },
                      "fifth": fifth
                      }
        field.value = test_input
        assert field.bytes == expected

    def test_len(self):
        """Test field length calculation"""
        field = self.field()
        assert len(field) == 4

    @pytest.mark.parametrize("item,value,expected", [
        ('first', 32, 32),
        ('third', 100, 100)
    ])
    def test_assignment(self, item, value, expected):
        """Test item assignment"""
        field = self.field()
        field[item] = value
        assert field[item].value == expected

    @pytest.mark.parametrize("item,value,expected", [
        ('sixth', 32, KeyError),
        ('second', 100, TypeError)
    ])
    def test_assignment_failed(self, item, value, expected):
        """Test failed item assignment"""
        field = self.field()
        with pytest.raises(expected):
            field[item] = value


class TestBitField:
    @pytest.fixture(scope='class')
    def field(self, *args, **kwargs):
        """Init empty test field"""
        from egts.egts_types import BitField, Bits
        return BitField(
            ("first", Bits(maxlen=1)),
            ("second", Bits(maxlen=5)),
            ("third", Bits(maxlen=2)),
            *args, **kwargs
        )

    @pytest.mark.parametrize("first,second,third,expected", [
        (1, 31, 3, 'ff'),
        (0b0, 0b00001, 0b00, '04')
    ])
    def test_str(self, first, second, third, expected):
        """Test field string request"""
        field = self.field()
        test_input = {"first": first,
                      "second": second,
                      "third": third
                      }
        field.value = test_input
        assert str(field) == expected

    @pytest.mark.parametrize("first,second,third,expected", [
        (-1, 0, 0, OverflowError),
        (0b10, 0, 0, OverflowError)
    ])
    def test_str_failed(self, first, second, third, expected):
        """Test failed string request"""
        field = self.field()
        test_input = {"first": first,
                      "second": second,
                      "third": third
                      }
        with pytest.raises(expected):
            field.value = test_input
            _ = str(field)

    @pytest.mark.parametrize("first,second,third,expected", [
        (1, 31, 3, b'\xff'),
        (0b0, 0b00001, 0b00, b'\x04')
    ])
    def test_bytes(self, first, second, third, expected):
        """Test field bytes request assignment"""
        field = self.field()
        test_input = {"first": first,
                      "second": second,
                      "third": third
                      }
        field.value = test_input
        assert field.bytes == expected

    def test_len(self):
        """Test field length calculation"""
        field = self.field()
        assert len(field) == 1

    @pytest.mark.parametrize("item,value,expected", [
        ('first', 0b1, 0b1),
        ('second', 0b10, 0b10)
    ])
    def test_assignment(self, item, value, expected):
        """Test item assignment"""
        field = self.field()
        field[item] = value
        assert field[item].value == expected

    @pytest.mark.parametrize("item,value,expected", [
        ('first', -1, OverflowError),
        ('second', 32, OverflowError)
    ])
    def test_assignment_failed(self, item, value, expected):
        """Test failed item assignment"""
        field = self.field()
        with pytest.raises(expected):
            field[item] = value


class TestArrayOfType:
    @pytest.fixture(scope='class')
    def field(self, *args, **kwargs):
        """Init empty test field"""
        from egts.egts_types import ArrayOfType, Byte
        return ArrayOfType(of_type=Byte, maxlen=4, *args, **kwargs)

    @pytest.mark.parametrize("input_list,expected", [
        ([10, 30, 40, 50], '0a1e2832'),
    ])
    def test_str(self, input_list, expected):
        """Test field string request"""
        field = self.field()
        field.value = input_list
        assert str(field) == expected

    @pytest.mark.parametrize("input_list,expected", [
        ([-1, 30, 40, 50], struct.error),
        ([0xff, 0x0a, 0xcc, None], ValueError),
        ([0xff, 0x0a, 0xcc, 0xcc, 0xcc], OverflowError)
    ])
    def test_str_failed(self, input_list, expected):
        """Test failed string request"""
        field = self.field()
        with pytest.raises(expected):
            field.value = input_list
            _ = str(field)

    @pytest.mark.parametrize("input_list,expected", [
        ([10, 30, 40, 50], b'\x0a\x1e\x28\x32'),
        ([0xff, 0x0a, 0xcc, 0x00], b'\xff\x0a\xcc\x00')
    ])
    def test_bytes(self, input_list, expected):
        """Test field bytes request assignment"""
        field = self.field()
        field.value = input_list
        assert field.bytes == expected

    def test_len(self):
        """Test field length calculation"""
        field = self.field()
        assert len(field) == 0
        field.append(5)
        assert len(field) == 1

    @pytest.mark.parametrize("initial_value,to_add,expected", [
        ([], 32, 32),
        ([1, 2, 3], '100', 100)
    ])
    def test_assignment(self, initial_value, to_add, expected):
        """Test item assignment"""
        field = self.field(value=initial_value)
        field.append(to_add)
        assert field[-1].value == expected

    @pytest.mark.parametrize("item,value,expected", [
        ([], 256, TypeError),
    ])
    def test_assignment_failed(self, item, value, expected):
        """Test failed item assignment"""
        field = self.field()
        with pytest.raises(expected):
            field[item] = value
