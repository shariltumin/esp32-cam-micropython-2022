
Currently, three ESP32-S3 camera boards are supported.

1. LILYGO-T-Camera-OV2640 N16R8 (Flash 16MB, PSRAM 8MB) 
2. XIAO-Sense-OV2640 N8R8 (Flash 8MB, PSRAM 8MB)
3. Freenove-OV2640 N8R8 (Flash 8MB, PSRAM 8MB)

The process of flashing the ESP32-S3 firmware is a bit different from that of the ESP32. It is possible that your Thonny IDE does not support ESP32-S3. You will have to use esptool.py to flash the firmware.

```
esptool.py --port /dev/ttyACM0 \
 --baud 460800 --before default_reset --after hard_reset \
 --chip esp32s3  write_flash --flash_mode dio --flash_size detect \
 --flash_freq 80m 0x0 firmware.bin

```

The LILYGO-T-camera board is a bit special. The OV2640 camera sensor gets its power from the AXP2101 PMU (Power Management Unit). This PMU must be set properly to power the OV2640. The firmware for the LILYGO-T camera has two extra frozen modules, I2CInterface.py and AXP2101.py, to help accomplish this task. I used the work of [Lewis](https://github.com/lewisxhe/XPowersLib/tree/master), thanks! You may also want to take a look at [this](https://github.com/Xinyuan-LilyGO/LilyGo-Cam-ESP32S3/tree/master).


