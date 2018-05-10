"""egts packet's main module"""
from . import *


def main():
    """Module Main Function"""
    egts_instance = EGTS()
    input_folder = 'D:\\PycharmProjects\\egts_protocol\\tests\\json\\result_code_simple.json'
    egts_instance.load_json(input_folder)
    output_folder = 'D:\\Shared\\test.hex'

    egts_instance.write(output_folder)
    print egts_instance
    print 'SUCCESS!'


main()
