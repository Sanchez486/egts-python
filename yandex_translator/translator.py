from egts.interface import *
from .wialon import *
from logger import Logger
import json
import socket
import os
import sys
import datetime


class Translator(object):
    """"Translator for itecorp"""

    DEF_SSOD = 0
    DEF_RSOD = 0
    DEF_SST = 2
    DEF_RST = 2

    DEF_BB = 0
    DEF_CS = 0
    DEF_FIX = 0
    DEF_VLD = 1
    DEF_ODM = "0x000000"
    DEF_DIN = "0b00000000"
    DEF_SRC = 0

    JSON_FILENAME = "msg.json"

    def __init__(self, detailed_logging=False):
        self.defaults = {
            'ssod': self.DEF_SSOD,
            'rsod': self.DEF_RSOD,
            'sst': self.DEF_SST,
            'rst': self.DEF_RST,
            'bb': self.DEF_BB,
            'cs': self.DEF_CS,
            'fix': self.DEF_FIX,
            'vld': self.DEF_VLD,
            'odm': self.DEF_ODM,
            'din': self.DEF_DIN,
            'src': self.DEF_SRC
        }
        self._logger = Logger(detailed_logging=detailed_logging)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._host = None
        self._port = None
        self._loaders = {
            'egts': self._load_egts,
            'wialon': self._load_wialon
        }

    def _load_egts(self, data):
        messages = []
        i = 0
        while i < len(data):
            if data[i] is None or data[i] == [] or data[i] == {}:
                continue
            data_record = data[i]

            i += 1

            msg = EGTS(codes.PacketType.EGTS_PT_APPDATA)
            msg.add_record(codes.SubrecordType.EGTS_SR_POS_DATA)
            msg_sdr = msg['sdr'][0]

            #  Generate Defaults
            for key in self.defaults.keys():
                msg_sdr[key] = self.defaults[key]

            rd = msg_sdr['rd'][0]

            msg_sdr['oid'] = data_record['id']
            msg_sdr['tm'] = datetime.datetime.now()
            msg_sdr['rn'] = i
            rd['ntm'] = data_record['ntm']
            rd['lat'] = data_record['lat']
            rd['long'] = data_record['long']
            rd['dir'] = data_record['dir']
            rd['spd'] = data_record['speed']
            rd['mv'] = int(data_record['speed'] > 0)
            messages.append(msg)
        return messages

    def _load_wialon(self, data):
        messages = []
        i = 0
        while i < len(data):
            if data[i] is None or data[i] == [] or data[i] == {}:
                continue
            packet_data = data[i]

            i += 1

            msg = WialonMessage()
            blocks_data = packet_data.pop('blocks')
            for key in packet_data:
                msg[key] = packet_data[key]
            for block_data in blocks_data:
                name = block_data.pop('name')
                if name == 'posinfo':
                    data_type = block_data.pop('type', 'posinfo')
                else:
                    data_type = block_data.pop('type')
                block = msg.add_block(name, data_type)
                for block_key in block_data.keys():
                    block[block_key] = block_data[block_key]
            messages.append(msg)

        return messages

    def load_json(self, json_path):
        json_file = open(json_path)
        json_data = json.load(json_file)
        self._host = json_data['server']
        self._port = json_data['port']
        protocol = json_data['protocol']
        data = json_data['data']
        self._logger.protocol = protocol
        return self._loaders[protocol](data)

    def send(self, data_bytes):
        self._socket.sendall(data_bytes)
        data = self._socket.recv(1024)
        res = b''
        for data_byte in data:
            res += data_byte.encode("hex")
        return res

    def run(self):
        current_path = os.path.dirname(os.path.abspath(sys.executable)) if sys.executable is not None else\
            os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        json_path = current_path + "\\" + self.JSON_FILENAME

        try:
            msgs = self.load_json(json_path)
            self._socket.connect((self._host, self._port))

            for msg in msgs:
                try:
                    reply_bytes = self.send(msg.bytes)
                    reply = ''
                    for reply_byte in reply_bytes:
                        reply += reply_byte
                    self._logger.log_reply(reply)
                except Exception as e:
                    self._logger.log_msg(str(e))

            self._socket.close()
        except Exception as e:
            self._logger._detailed_logging = True
            self._logger.log_msg(str(e))
        finally:
            self._logger.write(current_path)
