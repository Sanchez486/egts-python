import os
import time
import win32com.client
# import pytest
from egts.interface import egts


CWD = os.getcwd() + '\\'
VALIDATOR_FILENAME = 'EGTS_validator_x64.exe'
VALIDATOR = CWD + VALIDATOR_FILENAME
CMD = 'cmd.exe'
TIME = ['cmd.exe', '/C', 'time']
COMP = ['cmd.exe', '/C', 'comp']


def test_accel_data():
    msg = egts.EGTS()
    json_path = CWD + 'json/accel_data_simple.json'
    msg.load_json(json_path)
    msg_path = CWD + 'test.bin'
    msg.write(msg_path)

    print 'starting'

    validation_path = CWD + 'validation.txt'
    shell = win32com.client.Dispatch('WScript.Shell')
    shell.Run('cmd /C ' + VALIDATOR + ' -f:' + msg_path + ' > ' + validation_path)
    time.sleep(0.3)
    shell.SendKeys("{Enter}", 0)

    print 'finishing'

    assert str(msg)


test_accel_data()
