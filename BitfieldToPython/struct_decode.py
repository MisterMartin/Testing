import struct

# Define the format string for the BitFields struct
# Note: The format string is based on the layout of the struct in C++
#       'B' is for uint8_t, '?' is for bool, 'I' is for uint32_t, 'Q' is for uint64_t
#       The bit fields are handled by unpacking the bytes and then extracting the bits manually
format_string = 'B? ? ? B B B B B I I I I I I'

# Read the binary data from the file
with open('/Users/charlie/Testing/bitfields.bin', 'rb') as f:
    data = f.read()

# Unpack the data using the format string
unpacked_data = struct.unpack(format_string, data)

# Extract the bit fields manually
version = unpacked_data[0] & 0x1F
rs42_on = unpacked_data[0] >> 5 & 0x01
tsen_on = unpacked_data[0] >> 6 & 0x01
gps_on = unpacked_data[0] >> 7 & 0x01

# Print the decoded values
print(f'version: {version}')
print(f'rs42_on: {rs42_on}')
print(f'tsen_on: {tsen_on}')
print(f'gps_on: {gps_on}')
print(f'v1: {unpacked_data[1]}')
print(f'v2: {unpacked_data[2]}')
print(f'v3: {unpacked_data[3]}')
print(f't1: {unpacked_data[4]}')
print(f't2: {unpacked_data[5]}')
print(f'gps_lat: {unpacked_data[6]}')
print(f'gps_lon: {unpacked_data[7]}')
print(f'rs41_tdry: {unpacked_data[8]}')
print(f'rs41_pres: {unpacked_data[9]}')
print(f'rs41_hum: {unpacked_data[10]}')
print(f'tsen_tdry: {unpacked_data[11]}')
