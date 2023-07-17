These are the latest firmwares for MicroPython with camera based on esp-idf-445. The firmware version is v1.20.0-206-g33b403dfb. Newer versions of MicroPython will only build on esp-idf-5xx, the esp-idf-4xx versions are no longer supported.

I will freeze the camera firmware at v1.20.0-206 for now. Newer MicroPython based on esp-idf-502 still have some problems. I will build newer firmwares when these issues are fixed in the future.

Please refer to the [Note](https://github.com/shariltumin/esp32-cam-micropython-2022/blob/main/firmwares-20230717/Note.md) for information on the use of settings and functions in the camera module.

Subdirectory [ESP32](https://github.com/shariltumin/esp32-cam-micropython-2022/tree/main/firmwares-20230717/ESP32) contains firmwares for esp32-cam boards and subdirectory [ESP32-S3](https://github.com/shariltumin/esp32-cam-micropython-2022/tree/main/firmwares-20230717/ESP32-S3) contains firmwares for esp32-s3 boards. These firmwares only support the OV2640 sensor.

The MicroPython core team has now decided to drop the 'u' prefix from all modules. You can now do *import socket* instead of *import usocket as socket*.

These firmwares are not fully tested, my apologies in advance if they do not work as expected.
