
# The MIT License (MIT)
#
# Copyright (c) Sharil Tumin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#-----------------------------------------------------------------------------

# run this on ESP32 Camera

import esp
# from bluetooth import BLE
from Wifi import Sta
import socket as soc
import camera
from time import sleep

hdr = {
  # live stream -
  # URL: /live
  'stream': """HTTP/1.1 200 OK
Content-Type: multipart/x-mixed-replace; boundary=kaki5
Connection: keep-alive
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Expires: Thu, Jan 01 1970 00:00:00 GMT
Pragma: no-cache""",
  # live stream -
  # URL:
  'frame': """--kaki5
Content-Type: image/jpeg"""}

UID = const('ali')            # authentication user. Whatever you want
PWD = const('Baba40Robrs')    # authentication password. Whatever you want

cam = camera.init() # Camera
print("Camera ready?: ", cam)

# connect to access point
sta = Sta()              # Station mode (i.e. need WiFi router)
# sta.wlan.disconnect()    # disconnect from previous connection
AP = const('dlink-3530') # Your SSID
PW = const('cabbp73520') # Your password
sta.connect(AP, PW) # connet to dlink
sta.wait()

# wait for WiFi
con = ()
for i in range(5):
    if sta.wlan.isconnected():con=sta.status();break
    else: print("WIFI not ready. Wait...");sleep(2)
else:
    print("WIFI not ready")

if con and cam: # WiFi and camera are ready
   if cam:
     # set preffered camera setting
     camera.framesize(10)     # frame size 800X600 (1.33 espect ratio)
     camera.contrast(2)       # increase contrast
     camera.speffect(2)       # jpeg grayscale
   if con:
     # TCP server
     port = 80
     addr = soc.getaddrinfo('0.0.0.0', port)[0][-1]
     s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
     s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)
     s.bind(addr)
     s.listen(1)
     # s.settimeout(5.0)
     while True:
        cs, ca = s.accept()   # wait for client connect
        print('Request from:', ca)
        w = cs.recv(200) # blocking
        (_, uid, pwd) = w.decode().split('\r\n')[0].split()[1].split('/')
        # print(_, uid, pwd)
        if not (uid==UID and pwd==PWD):
           print('Not authenticated')
           cs.close()
           continue
        # We are authenticated, so continue serving
        cs.write(b'%s\r\n\r\n' % hdr['stream'])
        pic=camera.capture
        put=cs.write
        hr=hdr['frame']
        while True:
           # once connected and authenticated just send the jpg data
           # client use HTTP protocol (not RTSP)
           try:
              put(b'%s\r\n\r\n' % hr)
              put(pic())
              put(b'\r\n')  # send and flush the send buffer
           except Exception as e:
              print('TCP send error', e)
              cs.close()
              break
else:
   if not con:
      print("WiFi not connected.")
   if not cam:
      print("Camera not ready.")
   else:
      camera.deinit()
   print("System not ready. Please restart")

print('System aborted')
