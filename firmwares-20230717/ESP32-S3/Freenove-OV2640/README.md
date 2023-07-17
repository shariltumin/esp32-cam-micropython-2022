
# WiFi

This firmware supports WiFi with Socket/SSl, no BLE.

```
$ strings firmware.bin | grep IDF
MicroPython-1.20.0-xtensa-IDFv4.4.5-with-newlib3.3.0

$ strings firmware.bin | grep OV2640
; ESP32S3-FREENOVE OV2640 (KAKI5) with ESP32-S3

```

# WiFi+BLE

This firmware supports WiFi with Socket/SSl and BLE.

```
$ strings firmware.bin | grep IDF
MicroPython-1.20.0-xtensa-IDFv4.4.5-with-newlib3.3.0

$ strings firmware.bin | grep OV2640
; ESP32S3-FREENOVE OV2640 w/BLE (KAKI5) with ESP32-S3
```

--------------------------------------------------------

The firmware has the FREENOVE ESP32-S3-WROOM Camera pin configuration by default. A simple streaming server running on the camera board and an openCV client running on a Linux machine are provided as examples.

REPL is on the USB-OTG connector.

# Server
```
>>>
MPY: soft reboot
MicroPython v1.20.0-206-g33b403dfb-kaki5 on 2023-07-10; ESP32S3-FREENOVE OV2640 w/BLE (KAKI5) with ESP32-S3
>>> import streaming_server
Camera ready?:  True
Waiting ...
Waiting ...
Connected to dlink-3530
network config: ('192.168.4.74', '255.255.252.0', '192.168.4.1', '192.168.4.1')
Request from: ('192.168.4.27', 44764)
TCP send error [Errno 104] ECONNRESET

```

# Client
```
$ python streaming_client.py
Video stop

```

