"""egts packet's main module"""
from .interface import egts


def main():
    """Module Main Function"""
    egts_instance = egts.EGTS()
    input_folder = '/home/ailiush/PycharmProjects/egts_protocol' \
                   '/tests/test_command_data_conf.json'
    egts_instance.load_json(input_folder)
    output_folder = '/media/sf_Shared/test.hex'
    egts_instance.write(output_folder)

    print egts_instance
    print 'SUCCESS!'


main()
