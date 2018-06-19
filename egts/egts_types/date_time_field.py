from egts.egts_types import types
from datetime import datetime
import re


class DateTime(types.UInt):
    """
    Date-Time field which accepts datetime input and string time inputs
    """
    @property
    def _input_casts(self):
        """
        Add datetime cast in input casts
        :return: (input format: cast function) dict
        """
        casts = super(DateTime, self)._input_casts
        casts[datetime] = self._datetime_cast
        return casts

    def _datetime_cast(self, value):
        """
        Cast datetime value
        :param value: datetime value
        """
        initial_date = datetime(year=2010, month=1, day=1, hour=0, minute=0, second=0)
        seconds = int((value - initial_date).total_seconds())
        self._value = int(seconds)

    def _string_cast(self, value):
        """
        Cast string value.
        :param value: string value
        """
        try:
            mat = re.match('(\d{4})\-(\d{2})\-(\d{2})T(\d{2})\:(\d{2})\:(\d{2})$', value)
            if mat is not None:
                self._datetime_cast(datetime(*(map(int, mat.groups()))))
                return
        except ValueError:
            pass
        super(DateTime, self)._string_cast(value)
