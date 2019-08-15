from egts.egts_types import *
from egts.egts_types.date_time_field import DateTime
import calendar


class DateTimeBE(DateTime):
    @property
    def _format_char(self):
        """Encoded as unsigned short"""
        return '>L'

    def _datetime_cast(self, value):
        """
        Cast datetime value
        :param value: datetime value
        """
        self._value = calendar.timegm(value.timetuple())


class IntBE(Int):
    @property
    def _format_char(self):
        """Encoded as int"""
        return '>i'


class ShortBE(Short):
    @property
    def _format_char(self):
        """Encoded as short"""
        return '>h'


class LongBE(ULong):
    @property
    def _format_char(self):
        """Encoded as long"""
        return '>l'


class StringZero(String):
    def _string_cast(self, value):
        """
        Cast string value.
        :param value: string value
        """
        self._value = value + '\x00'

    def _unicode_cast(self, value):
        self._string_cast(value.encode('utf-8'))
