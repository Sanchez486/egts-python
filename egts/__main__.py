"""egts packet's main module"""
from .interface import egts
import os


def main():
    """Module Main Function"""
    egts_instance = egts.EGTS()
    input_folder = 'D:\\PycharmProjects\\egts_protocol\\tests\\json\\track_data_and_accel_data.json'
    egts_instance.load_json(input_folder)
    output_folder = 'D:\\Shared\\test.hex'
    egts_instance.write(output_folder)

    print egts_instance
    print 'SUCCESS!'


main()
