Firmware with BLE only, without WiFi

```
MicroPython v1.20.0-39-g61b8e1b2d-kaki5 on 2023-05-20; ESP32 CAMERA BLE (KAKI5) module with ESP32
>>> import camera
>>> import bluetooth
>>> bluetooth.
BLE             FLAG_INDICATE   FLAG_NOTIFY     FLAG_READ
FLAG_WRITE      FLAG_WRITE_NO_RESPONSE          UUID
>>> ble = bluetooth.BLE()
>>> ble.
active          config          gap_advertise   gap_connect
gap_disconnect  gap_pair        gap_passkey     gap_scan
gattc_discover_characteristics  gattc_discover_descriptors
gattc_discover_services         gattc_exchange_mtu
gattc_read      gattc_write     gatts_indicate  gatts_notify
gatts_read      gatts_register_services         gatts_set_buffer
gatts_write     irq
>>> camera.
aecvalue        aelevels        agcgain         brightness
capture         conf            contrast        deinit
flip            framesize       init            mirror
pixformat       quality         saturation      speffect
whitebalance
>>> camera.init()
E (33556) gpio: gpio_install_isr_service(449): GPIO isr service already installed
True
>>> img=camera.capture()
>>> len(img)
13634
>>> camera.framesize(11)
>>> img=camera.capture()
>>> len(img)
18141
>>> camera.framesize(13)
>>> img = camera.capture()
>>> img = camera.capture()
E (184114) camera: Camera Capture Failed
>>> img = camera.capture()
E (192574) camera: Camera Capture Failed
```

I am interested to know how you are using camera module with BLE. Please share your projects.
