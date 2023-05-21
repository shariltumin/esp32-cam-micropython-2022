Firmware with WiFI/SSL only, no bluetooth.BLE

```
MicroPython v1.20.0-39-g61b8e1b2d-kaki5 on 2023-05-20; ESP32 CAMERA w/SSL (KAKI5) with ESP32
>>> import camera
>>> camera.
aecvalue        aelevels        agcgain         brightness
capture         conf            contrast        deinit
flip            framesize       init            mirror
pixformat       quality         saturation      speffect
whitebalance
>>> img = camera.capture()
>>> len(img)
69153
>>> camera.framesize(13)
>>> img = camera.capture()
>>> len(img)
95050
>>> import ssl
>>> ssl.
CERT_NONE       CERT_OPTIONAL   CERT_REQUIRED   wrap_socket
>>> import bluetooth
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: no module named 'bluetooth'

```
