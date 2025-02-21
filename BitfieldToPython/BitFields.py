# Give me an example of Python source code to decode the BitFields struct from an array of bytes to a type safe dataclass. Use python bool type hinting.

# Python code to decode the BitFields struct from an array of bytes

import struct

from dataclasses import dataclass

@dataclass
class BitFields:
    version: int
    rs42_on: bool
    tsen_on: bool
    gps_on: bool
    v1: int
    v2: int
    v3: int
    t1: int
    t2: int
    gps_lat: int
    gps_lon: int
    rs41_tdry: int
    rs41_pres: int
    rs41_hum: int
    tsen_tdry: int

def decode_bitfields(data):
    bitfields_format = (
        'B'  # version, rs42_on, tsen_on, gps_on
        'B'  # v1
        'B'  # v2
        'B'  # v3
        'B'  # t1
        'B'  # t2
        'I'  # gps_lat
        'I'  # gps_lon
        'I'  # rs41_tdry
        'I'  # rs41_pres
        'I'  # rs41_hum
        'I'  # tsen_tdry
    )
    
    print(len(data))
    unpacked_data = struct.unpack(bitfields_format, data)
    
    bitfields = BitFields(
        version=(unpacked_data[0] >> 4) & 0x0F,
        rs42_on=bool((unpacked_data[0] >> 3) & 0x01),
        tsen_on=bool((unpacked_data[0] >> 2) & 0x01),
        gps_on=bool((unpacked_data[0] >> 1) & 0x01),
        v1=unpacked_data[1],
        v2=unpacked_data[2],
        v3=unpacked_data[3],
        t1=unpacked_data[4],
        t2=unpacked_data[5],
        gps_lat=unpacked_data[6],
        gps_lon=unpacked_data[7],
        rs41_tdry=unpacked_data[8] & 0x3FFFF,
        rs41_pres=unpacked_data[9] & 0x3FFFF,
        rs41_hum=unpacked_data[10] & 0x3FFFF,
        tsen_tdry=unpacked_data[11] & 0x3FFFF,
    )
    
    return bitfields

# Example usage:
data = b'\x12\x34\x56\x78\x9A\xBC\xDE\xF0\x12\x34\x56\x78\x9A\xBC\xDE\xF0\x12\x34\x56\x78\x12\x34\x56\x78\x9A\xBC\xDE\xF0\x12\x34\x56\x78'
decoded = decode_bitfields(data)
print(decoded)
