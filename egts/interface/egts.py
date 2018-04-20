"""MAIN EGTS INTERFACE"""
import json
import enum
from ..egts_message import EGTSMessage
from . import classes


class EGTS(object):
    """EGTS Message interface"""
    def __init__(self, packet_type=None):
        """Constructor"""
        self._message = EGTSMessage()
        if packet_type:
            self.set_packet_type(packet_type)

    def __str__(self):
        """
        Get message's octet string
        :return: octet string
        """
        return str(self._message)

    def load_json(self, json_path):
        """
        Read EGTS message from json
        :param json_path: file to read
        """
        json_file = open(json_path)
        egts = json.load(json_file)
        # <FIX>
        if egts['service']:
            self.set_packet_type(egts['transport']['pt'])
            for record in egts['service']['sdr']:
                types = list()
                for subrecord in record['rd']:
                    types.append(subrecord['srt'])
                self.add_record(*types)
        # </FIX>
        self._message.value = egts

    def write(self, output_folder):
        """
        Write the message to raw byte file
        :param output_folder: path to write
        """
        output_file = open(output_folder, 'wb')
        for each_byte in self._message.bytes:
            output_file.write(chr(each_byte))

    def set_packet_type(self, packet_type):
        """
        Specify message's packet type
        :param packet_type: type of packet (int/enum)
        """
        if isinstance(packet_type, enum.Enum):
            pt = packet_type.value
        else:
            pt = packet_type
        self._message['service'] = classes.packet_types[pt]()

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
