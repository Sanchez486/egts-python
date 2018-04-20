import os
import pytest
from egts.interface import egts


CWD = os.getcwd()


def test_accel_data():
    msg = egts.EGTS()
    msg.load_json(CWD + '/json/test_accel_data.json')
    assert str(msg)
