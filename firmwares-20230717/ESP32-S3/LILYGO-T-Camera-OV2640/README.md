
# WiFi

This firmware supports WiFi with Socket/SSl, no BLE.

```
$ strings firmware.bin | grep IDF
MicroPython-1.20.0-xtensa-IDFv4.4.5-with-newlib3.3.0

$ strings firmware.bin | grep OV2640
; ESP32S3-LILYGO T-Cam OV2640 (KAKI5) with ESP32-S3

```

# WiFi+BLE

This firmware supports WiFi with Socket/SSl and BLE.

```
$ strings firmware.bin | grep IDF
MicroPython-1.20.0-xtensa-IDFv4.4.5-with-newlib3.3.0

$ strings firmware.bin | grep OV2640
; ESP32S3-LILYGO T-Cam OV2640 w/BLE (KAKI5) with ESP32-S3

```

--------------------------------------------------------

Lilygo T-Camera needs PMU to work!

The project uses the work of Lewis He (lewishe@outlook.com) from:

https://github.com/lewisxhe/XPowersLib/tree/master

and the example from:

https://github.com/Xinyuan-LilyGO/LilyGo-Cam-ESP32S3/tree/master

The firmware has the Lilygo T-Camera pin configuration by default. A simple streaming server running on the camera board and an openCV client running on a Linux machine are provided as examples.

# Server
```
>>>
MPY: soft reboot
MicroPython v1.20.0-206-g33b403dfb-kaki5 on 2023-07-13; ESP32S3-LILYGO T-Cam OV2640 w/BLE (KAKI5) with ESP32-S3
>>> import streaming_server
micropython
AXP2101 __init__
getID:0x4a
Camera ready?:  True
Waiting ...
Waiting ...
Connected to dlink-3530
network config: ('192.168.4.71', '255.255.252.0', '192.168.4.1', '192.168.4.1')
Request from: ('192.168.4.27', 50740)
TCP send error [Errno 104] ECONNRESET

```

# Client
```
$ python streaming_client.py
Video stop

```

