Firmware with Bluetooth Classic, not included BLE and WiFI.

```
MicroPython v1.20.0-39-g61b8e1b2d-kaki5 on 2023-05-23; ESP32 CAMERA Bluetooth Classic (KAKI5) module with ESP32
>>> dir()
['uos', 'gc', '__name__', 'bdev']
>>> gc.mem_free()
2175168
>>> import bts
>>> bts.
close           __dict__        data            deinit
get_bin         get_str         init            ready
send_bin        send_str        up
>>> gc.mem_free()
2174848
>>> bts.init("SLV-1", "2761")
True
>>> bts.up()
True
>>> import camera
>>> camera.init()
E (448640) gpio: gpio_install_isr_service(449): GPIO isr service already installed
True
>>> bts.data()    
5
>>> w=bts.get_str(100) 
>>> w
'hello'
>>> bts.ready()
True
>>> bts.send_bin(b'ok') 
>>> img=camera.capture()
>>> gc.mem_free()
2121040

```

More information about Bluetooth Classic module can be founnd [here](https://github.com/shariltumin/esp32-bluetooth-classic-micropython). 
