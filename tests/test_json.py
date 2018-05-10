import os
import time
import win32com.client
import pytest
from egts.interface import egts


CWD = os.getcwd() + '\\'
VALIDATOR_FILENAME = 'EGTS_validator_x64.exe'
VALIDATOR_PATH = '{}json\\{}'.format(CWD, VALIDATOR_FILENAME)


TEST_NAMES = [
    'ad_sensors_data_simple',
    'accel_data_simple',
    'accel_data_max_size',
    'auth_info_simple',
    'auth_params_max_size',
    'auth_params_no_optional',
    # VALIDATOR CRASH: 'command_data_max_size_com',
    # VALIDATOR CRASH: 'command_data_max_size_conf',
    'command_data_simple_com',
    'command_data_simple_conf',
    'counters_data_simple',
    'module_data_simple',
    'raw_msd_data_max_length',
    'raw_msd_data_simple',
    'result_code_simple',
    'service_full_data_max_size',
    'service_full_data_simple',
    'service_info_simple',
    'service_part_data_max_size',
    'service_part_data_simple',
    'term_identity_all_optional',
    'term_identity_max_size',
    'term_identity_no_optional',
    'term_identity_simple',
    'track_data_and_accel_data',
    'track_data_empty',
    'track_data_max_size',
    'track_data_simple',
    'transport',
    'vehicle_data_and_term_identity',
    'vehicle_data_simple',
]


@pytest.mark.parametrize("test_name", TEST_NAMES)
def test_json(test_name):
    def wait(tm):
        time.sleep(tm/10.)

    # Write Test Message File
    msg = egts.EGTS()
    json_path = '{}json\\data\\{}.json'.format(CWD, test_name)
    msg.load_json(json_path)
    msg_path = '{}json\\generated\\tmp_msg.bin'.format(CWD)
    msg.write(msg_path)

    # Generate Validator Output
    result_path = '{}json\\generated\\{}.txt'.format(CWD, test_name)
    shell = win32com.client.Dispatch('WScript.Shell')
    shell.Run('cmd /C ' + VALIDATOR_PATH + ' -f:' + msg_path + ' > ' + result_path)
    wait(1)
    shell.SendKeys("{Enter}", 0)
    wait(1)

    # Compare output with expected
    expected_path = '{}json\\expected\\{}.txt'.format(CWD, test_name)
    if os.path.isfile(expected_path):
        result = open(result_path, 'r')

        expected = open(expected_path, 'r')
        assert result.readlines()[3:] == expected.readlines()[3:]
    else:
        raise NotImplementedError('{} do not have any expected output!'.format(test_name))
