from st7735M import TFT,TFTColor
from machine import SPI,Pin,Signal
from time import sleep
import camera
import cam_config as cc

# set camera configuration
cc.configure(camera, cc.ai_thinker)
camera.conf(cc.PIXFORMAT,cc.PIXFORMAT_RGB565) # both pixformat and 
camera.conf(cc.FRAMESIZE,cc.FRAMESIZE_QQVGA) # framesize MUST before camera.init
camera.init()

# other setting after init
camera.quality(12)
camera.speffect(2) # black and white
spi = SPI(1, baudrate=60000000, polarity=0, phase=0)
tft=TFT(spi,2,15,12)
tft.init_7735(tft.GREENTAB80x160)
tft.fill(TFT.BLACK)
def display():
     w,h=160-1,80-1
     s0=160*20*2
     sx=160*100*2
     loc=tft._setwindowloc
     take=camera.capture
     put=tft._writedata
     while True:
         img=take()
         loc((0,0),(w,h))
         put(img[s0:sx])
 
display()
