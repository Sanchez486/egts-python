"""MAIN EGTS INTERFACE"""
import json
import enum
from ..egts_message import EGTSMessage
from . import classes


class EGTS(object):
    """EGTS Message interface"""
    def __init__(self, packet_type=None, *records):
        """Constructor"""
        self._message = EGTSMessage()
        if packet_type:
            self.set_packet_type(packet_type)
            for subrecords in records:
                self.add_record(*subrecords)

    def __str__(self):
        """
        Get message's octet string
        :return: octet string
        """
        return str(self._message)

    @property
    def bytes(self):
        """
        Get message's bytes representation
        :return: byte string
        """
        return self._message.bytes

    def __getitem__(self, item):
        return self._message[item]

    def __setitem__(self, key, value):
        self._message[key] = value

    def load_json(self, json_path):
        """
        Read EGTS message from json
        :param json_path: file to read
        """
        json_file = open(json_path)
        egts = json.load(json_file)
        if 'service' in egts:
            self.set_packet_type(egts['transport']['pt'])
            for record in egts['service']['sdr']:
                types = list()
                for subrecord in record['rd']:
                    types.append(subrecord['srt'])
                self.add_record(*types)
        else:
            self._message._value.pop('service')
            self._message._value.pop('sfrcs')
        self._message.value = egts
        if not self._message.is_ready():
            raise ValueError('Incomplete JSON! Some required fields are unspecified!')

    def write(self, output_folder):
        """
        Write the message to raw byte file
        :param output_folder: path to write
        """
        output_file = open(output_folder, 'wb')
        output_file.write(self.bytes)

    def set_packet_type(self, packet_type):
        """
        Specify message's packet type
        :param packet_type: type of packet (int/enum)
        """
        if isinstance(packet_type, enum.Enum):
            pt = packet_type.value
        else:
            pt = packet_type
        try:
            self._message['service'] = classes.packet_types[pt]()
            self._message['transport']['pt'] = pt
        except KeyError:
            raise TypeError('Unknown packet type: {}'.format(pt))

    def add_record(self, *subrecord_types):
        """
        Add new record to the message
        :param subrecord_types:
        :return:
        """
        sdr = self._message['sdr']
        sdr.append()
        record_number = sdr.quantity - 1
        for subrecord_type in subrecord_types:
            self.add_subrecord(record_number, subrecord_type)
        return sdr[record_number]

    def add_subrecord(self, record_number, subrecord_type):
        """
        Add subrecord to the record
        :param record_number: number of record to add to
        :param subrecord_type: subrecord type to add
        """
        record = self._message['sdr'][record_number]
        srd = record['rd']
        srd.append()
        subrecord_number = srd.quantity - 1

        if isinstance(subrecord_type, enum.Enum):
            srt = subrecord_type.value
        else:
            srt = subrecord_type
        srd[subrecord_number]['srd'] = classes.subrecord_types[srt]()
        srd[subrecord_number]['srt'] = srt
        return srd[subrecord_number]
