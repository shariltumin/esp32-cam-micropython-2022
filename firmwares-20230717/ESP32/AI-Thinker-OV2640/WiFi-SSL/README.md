
# WiFi w/SSL
```
$ strings firmware.bin | grep IDF
MicroPython-1.20.0-xtensa-IDFv4.4.5-with-newlib3.3.0

$ strings firmware.bin | grep KAKI5
; ESP32 CAMERA w/SSL (KAKI5) with ESP32
```

The firmware has the AI-Thinker Camera pin configuration by default. A simple streaming server running on the camera board and an openCV client running on a Linux machine are provided as examples.

# Server
```
$ tio /dev/ttyUSB0

>>> 
MPY: soft reboot
MicroPython v1.20.0-206-g33b403dfb-kaki5 on 2023-07-11; ESP32 CAMERA w/SSL (KAKI5) with ESP32
>>> import streaming_server
Camera ready?:  True
Waiting ...
Waiting ...
Connected to dlink-3530
network config: ('192.168.4.48', '255.255.252.0', '192.168.4.1', '192.168.4.1')
Request from: ('192.168.4.27', 38962)
TCP send error [Errno 104] ECONNRESET

```
# Client

```
$ python streaming_client.py
Video stop

```
