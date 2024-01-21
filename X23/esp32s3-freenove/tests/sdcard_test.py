
from machine import SDCard
import os

sd = SDCard(slot=1, cd=None, wp=None)
sd.info()
# (1006632960, 512)
os.mount(sd, '/sd')

import camera
cam = camera.init()
if not cam:
   print('Hard reset!!')
   from machine import reset
   reset()

img = camera.capture()
print('Image size:', len(img))
with open('/sd/img1.jpg', 'wb') as f:
     w = f.write(img)
     print('Bytes saved:', w)
print(os.listdir('/sd'))
# ['img1.jpg']
os.umount('/sd')
camera.deinit()

