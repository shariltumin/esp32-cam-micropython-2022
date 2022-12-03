
MicroPython v1.19.1-705-gac5934c96-kaki5 on 2022-12-03; ESP32 CAMERA w/SSL

This firmware has the support of SSL. It is experiential. It has not been properly tested for sending a JPEG image to a proper server over SSL.

The following test script simply checks whether we have enough runtime RAM when WIFI, camera, and SSL are loaded. 

```
import network
import usocket as _socket
import ussl as ssl
import camera

camera.init()

network.WLAN(network.AP_IF).active(False)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("your SSID", "your PWD")

img=camera.capture()

s = _socket.socket()
ai = _socket.getaddrinfo("micropython.org", 443)
addr = ai[0][-1]
print("Connect address:", addr)
s.connect(addr)
s = ssl.wrap_socket(s)
s.write(b"GET / HTTP/1.0\r\n\r\n")
print(s.read(1024))

print(len(img))
```

When everything is working properly, you will receive 1 KB from micropython.org as well as a number representing the length of the image captured earlier in the script. 

