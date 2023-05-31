
import camera, machine, uos
from esp32_ble import BLE
import time

# init camera
cam = camera.init()
if cam:
   print("Camera ready?: ", cam)
else:
   camera.deinit()
   machine.reset() # just reset

# set preffered camera setting
camera.framesize(10)     # frame size 800X600 (1.33 espect ratio)
camera.contrast(2)       # increase contrast
camera.speffect(2)       # jpeg grayscale
img=camera.capture()     # throw away 1.st frame

# init ble
ble = BLE("ESP32-KAKI5")

# mount sdcard
sd=machine.SDCard(slot=1)
uos.mount(sd, "/sd")

max_frames = 500 # max(whatever you want) limit 9999 & card capacity 
cnt = 0
grab = False 
idx = 0
fn = ''
f = None

while 1:
   msg = ble.get_message()
   if msg: # not ''
      if msg == 'start':  # start/resart recoding
         grab = True
      elif msg == 'stop': # stop recording
         grab = False
      elif msg == 'bye': 
         grab = False
         break # break out of loop
      else:
         pass # do nothing
   if grab:
      fn = '/sd/pic-%04d.jpg'%idx  # max: pic-9999.jpg
      f = open(fn, 'wb')
      img=camera.capture()
      if len(img) > 0 and f:
         f.write(img)
         print('Frame:', idx)
         idx += 1
      f.close()
      f = None
      if idx>max_frames: # guard
         grab = False
         break # breakout limit reached
   else:
      #time.sleep_ms(30) # every 30 ms
      pass # as fast as possible
if f:
   f.close()

uos.listdir("/sd")
uos.umount("/sd")
camera.deinit()
