#include <stdint.h>


#include <iostream>
#include <fstream>

int main() {

    typedef struct {
        uint8_t version : 4;
        bool rs42_on : 1;
        bool tsen_on : 1;
        bool gps_on : 1;
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
    
    // Create and populate the BitFields structure
    BitFields data;
    data.version = 12;
    data.rs42_on = true;
    data.tsen_on = false;
    data.gps_on = true;
    data.v1 = 10;
    data.v2 = 20;
    data.v3 = 30;
    data.t1 = 40;
    data.t2 = 255;
    data.gps_lat = 123456789;
    data.gps_lon = 987654321;
    data.rs41_tdry = 100000;
    data.rs41_pres = 200000;
    data.rs41_hum = 262143;
    data.tsen_tdry = 262142;

    // Write the structure to a file
    std::ofstream outfile("/Users/charlie/Testing/bitfields.bin", std::ios::binary);
    if (outfile.is_open()) {
        outfile.write(reinterpret_cast<char*>(&data), sizeof(data));
        outfile.close();
        std::cout << "Data written to file successfully." << std::endl;
    } else {
        std::cerr << "Failed to open file for writing." << std::endl;
    }

    return 0;
}