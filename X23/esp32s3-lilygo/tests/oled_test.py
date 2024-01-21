
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

from machine import reset, SoftI2C, Pin
from pmu import cam_power_on
import ssd1306f
import camera
import cam_config as cc
from time import sleep

# Switch on camera power controlled by AXP2101
cam_power_on()

# camera
camera.conf(cc.FRAMESIZE, cc.FRAMESIZE_QQVGA) # 160x120
camera.conf(cc.PIXFORMAT, cc.PIXFORMAT_GRAYSCALE)
cam = camera.init()

if not cam:
   print('No camera. Hard reset!!')
   sleep(5)
   reset()

# liligo t-camera board
i2c = SoftI2C(Pin(6), Pin(7)) # id, scl, sda
# i2c.scan() # [52, 60]
display = ssd1306f.SSD1306_I2C(128, 64, i2c)

@micropython.native
def see(): # 
   # display.invert(1) # 1 invert / 0 normal
   while True:
      img=camera.capture_bmp()[160*10:]      # skip 10 rows from image
      for dark in (115, 125, 120, 117, 122): # dark threshold values, your choice
                                             # to simulate grayscale
          for y in range(64):
              cnt=160*y
              for x in range(128):
                display.pixel(x,y,(0 if img[cnt]<dark else 1))
                cnt+=1
          display.show()

print('Ready, system start')
try:
   see() # start
except:
   print('System aborted. Hard reset!!')
   sleep(1)
   reset()
   


