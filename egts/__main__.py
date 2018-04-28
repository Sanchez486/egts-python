"""egts packet's main module"""
from .interface import egts
from .interface import codes


def main():
    """Module Main Function"""
    egts_instance = egts.EGTS()
    input_folder = 'D:\\PycharmProjects\\egts_protocol\\tests\\json\\track_data_simple.json'
    egts_instance.load_json(input_folder)
    output_folder = 'D:\\Shared\\test.hex'
    egts_instance.write(output_folder)

    import struct
    num = -1.2e-45
    res = struct.pack('<f', num).encode('hex')
    res2 = struct.unpack('<f', res.decode('hex'))
    print res
    print res2

    print egts_instance
    print 'SUCCESS!'


main()
