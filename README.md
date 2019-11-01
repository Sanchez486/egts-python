# EGTS Packet Encoder
**Python library for encoding vehicle data to EGTS packets**

## Required packages:
 * enum

## Installation
1. Rename "_setup_egts.py_" to "_setup.py_"
2. Run "_python setup.py_"
3. After setup is done run "_pip install ._"

## Usage
 * To create a EGTS message use **EGTS** class from _interface_ package: `from egts.interface.egts import EGTS`
 * For manual data assignment:
   * Use the _codes_ module to get EGTS protocol codes: `from egts.interface import codes`
   * You **must** specify Packet Types and Subrecord Types: <br />
     * In constructor: <br />
     ```python
     msg = EGTS(PacketType.EGTS_PT_APPDATA, (SubrecordType.EGTS_SR_ACCEL_DATA,), (SubrecordType.EGTS_SR_TRACK_DATA, SubrecordType.EGTS_SR_TRACK_DATA))
     ```
     This command creates a EGTS_PT_APPDATA packet with two records:
     record #1 has one EGTS_SR_ACCEL_DATA subrecord;
     record #2 has two EGTS_SR_TRACK_DATA subrecords <br />
     **OR**
     * Via _set_packet_type_, _add_record_ and _add_subrecord_ methods: <br />
     ```python
     msg = EGTS()
     msg.set_packet_type(PacketType.EGTS_PT_APPDATA)
     record1 = msg.add_record((SubrecordType.EGTS_SR_ACCEL_DATA,))
     record2 = msg.add_record()
     subrecord1 = record2.add_subrecord(SubrecordType.EGTS_SR_TRACK_DATA)
     subrecord2 = record2.add_subrecord(SubrecordType.EGTS_SR_TRACK_DATA)
     ```
   * To work with a specific record within a packet, retrieve it using the number of the record:
   ```python
   record1 = msg[0]
   ```
   * To work with a specific subrecord within a record, retrieve it using the number of the record:
   ```python
   subrecord1 = record1[0]
   ```
   * Use `__setitem__` to set field values, there is a deep search so you don't have to retrieve compound fields every time:
   ```python
   subrecord1['cid'] = 1
   subrecord1['cct'] = 0 # does the same that subrecord1['type_flags']['cct'] = 0
   ```
   * You can use `__getitem__` to get fields if neccessary:
   ```python
   flags = subrecord1['type_flags']
   flags['cct'] = 0
   ```
 * For JSON assignment:
   * Use `load_json` method:
   ```python
   msg = EGTS()
   msg.load_json('/home/sanchez486/data.json')
   ```
   You can find json examples in `/tests/json/data` folder
 * Use `__str__` to get a EGTS packet byte string:
 ```python
 egts_string = str(msg)
 pring egts_string # 0100000B0012000100018807000100040000D90F0202180400010203047EB2
 ```
 * Use `bytes` property to get packet representation in bytes:
  ```python
 egts_bytes = msg.bytes
 ```
  * Use `write` method to write the packet bytes in a file:
  ```python
 msg.write('/home/sanchez486/data.hex')
 ```

## Contacts
I apologize for confusing import names and weird installation instructions. I didn't have a chance to create some order in the packages.
The library was not properly tested with a real gear so it may show some unexpected behavior. If you have any questions, suggestions or fix requests please free to contact me in github or via these credentials:
 * E-mail: fergusonalexandr@mail.ru
 * Skype: live:ailiush
 * Vk: https://vk.com/sanchez486

