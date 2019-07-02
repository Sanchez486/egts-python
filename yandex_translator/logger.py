import json


class Logger(object):
    FILENAME = 'response.json'

    def __init__(self, detailed_logging=False):
        self._logs = []
        self._detailed_logging = detailed_logging

    def log_msg(self, msg):
        self._logs.append(msg)

    @staticmethod
    def get_bytes(msg):
        byte_arr = []
        for i in xrange(0, len(msg), 2):
            byte_arr.append(int(msg[i:i+2], 16))
        return byte_arr

    @staticmethod
    def get_big_endian_int(bytestr):
        reverse_bytestr = ''
        for i in xrange(0, len(bytestr), 2):
            reverse_bytestr = bytestr[i:i+2] + reverse_bytestr
        return int(reverse_bytestr, 16)

    def log_reply(self, response):
        if response[:2] != '01':
            self.log_msg(response)
            return
        sr = response[-12:-4]
        subrecord_type = int(sr[:2], 16)
        result_code = int(sr[-3:], 16)
        if result_code != 0 or subrecord_type != 0:
            self.log_msg(response)
        else:
            self.log_msg('ok')

    def write(self, path):
        res = self._logs
        if not self._detailed_logging:
            for i in xrange(0, len(res)):
                if res[i] != 'ok':
                    res[i] = 'error'
        output_file = open(path + '\\' + self.FILENAME, 'wb')
        json.dump(res, output_file)

    def clean(self):
        self._logs = []
