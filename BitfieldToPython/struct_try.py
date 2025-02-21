#ifndef STRUCT_H
#define STRUCT_H

#include <stdint.h>

struct {
    uint8_t version : 4;
    uint8_t rs42_on : 1;
    uint8_t tsen_on : 1;
    uint8_t gps_on : 1;
    uint8_t v1 : 8;
    uint8_t v2 : 8;
    uint8_t v3 : 8;
    uint8_t t1 : 8;
    uint8_t t2 : 8;
    uint64_t gps_lat : 32;
    uint64_t gps_lon : 32;
    uint32_t rs41_tdry : 18;
    uint32_t rs41_pres  : 18;
    uint32_t rs41_hum : 18;
    uint32_t tsen_tdry : 18;
} BitFields;

// Give me an example of Python source code to decode the BitFields struct from an array of bytes
import struct

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
    
    unpacked_data = struct.unpack(bitfields_format, data)
    
    bitfields = {
        'version': (unpacked_data[0] >> 4) & 0x0F,
        'rs42_on': (unpacked_data[0] >> 3) & 0x01,
        'tsen_on': (unpacked_data[0] >> 2) & 0x01,
        'gps_on': (unpacked_data[0] >> 1) & 0x01,
        'v1': unpacked_data[1],
        'v2': unpacked_data[2],
        'v3': unpacked_data[3],
        't1': unpacked_data[4],
        't2': unpacked_data[5],
        'gps_lat': unpacked_data[6],
        'gps_lon': unpacked_data[7],
        'rs41_tdry': unpacked_data[8] & 0x3FFFF,
        'rs41_pres': unpacked_data[9] & 0x3FFFF,
        'rs41_hum': unpacked_data[10] & 0x3FFFF,
        'tsen_tdry': unpacked_data[11] & 0x3FFFF,
    }
    
    return bitfields

# Example usage:
# data = b'\x12\x34\x56\x78\x9A\xBC\xDE\xF0\x12\x34\x56\x78\x9A\xBC\xDE\xF0\x12\x34\x56\x78'
# decoded = decode_bitfields(data)
# print(decoded)

#endif // STRUCT_H
