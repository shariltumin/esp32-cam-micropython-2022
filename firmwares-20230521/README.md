Here are 2 firmwares for MicroPython v1.20.0-39. They were compiled with ESP-IDFv4.4.4.
1. WIFI+TLS (Wifi with SSL, without BLE)
2. BLE (Bluetooth BLE, without Wifi)

You decide which one you require for your projects. There is no firmware that supports both WiFi and Bluetooth Low Energy.

The camera module now has an additional method camera.conf(). You can use it to set the camera configuration, such as PINs, camera CLOCK, format and framesize. This should be done before calling camera.init(). See the scripts/config.pyconfig.py file for details. How to use it

```python
import camera
import config as K

camera.conf(K.XCLK_MHZ, 14) # 14Mhz xclk rate
cam = camera.init()

img = img = camera.capture()

```

The firmwares have been compiled with the AI-Thinker esp32-cam board as default configuration. They only support the OV2640. If you have a different configuration, it is possible to define a custom configuration in the config.py, for example wrover_test. To set up your camera, just follow this code sequence

```python
import camera
import config as K

K.configure(camera, K.wrover_test)
cam = camera.init()

img = img = camera.capture()

```

I am working on firmwares for esp32-wrover, esp32-s2, esp32-s3 with OV7670, OV2640 and OV5640. The camera.conf() and config.py is a step in that direction.
