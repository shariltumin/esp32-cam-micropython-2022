
On-board SD Card reader

```py
>>> from machine import SDCard
>>> sd = SDCard(slot=1, cd=None, wp=None)
>>> sd.info()
(1006632960, 512)
>>> os.mount(sd, '/sd')
>>> import camera
>>> camera.init()
True
>>> img = camera.capture()
>>> len(img)
13288
>>> with open('/sd/img1.jpg', 'wb') as f:
...     f.write(img)
... 
13288
>>> os.listdir('/sd')
['img1.jpg']
>>> os.umount('/sd')
>>> camera.deinit()
True
>>> 
MPY: soft reboot

```

We have http-based streaming server

```py
>>> 
>>> import streaming_server
Camera ready?:  True
WIFI not ready. Wait...
WIFI not ready. Wait...
WIFI ready
('192.168.4.74', '255.255.252.0', '192.168.4.1', '192.168.4.1')
Request from: ('192.168.4.27', 34080)
TCP send error [Errno 113] ECONNABORTED
Request from: ('192.168.4.27', 36656)
```

Now and then you might get "[Errno 113] ECONNABORTED". I don't know why the esp32s3 board got disconnect from the router. One thing for sure is that power supply and the board placement relative to the WiFi router can play some roles on how stable the the connection is.


