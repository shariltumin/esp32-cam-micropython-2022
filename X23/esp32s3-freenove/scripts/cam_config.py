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

from micropython import const

def configure(cam, config):
    for key, val in config.items():
        # print(key, val)
        cam.conf(key, val)

#-camera configuration int keys ** DONT EDIT **---------------
PIN_PWDN    = const(0) # power-down 
PIN_RESET   = const(1) # reset
PIN_XCLK    = const(2)
PIN_SIOD    = const(3) #  SDA
PIN_SIOC    = const(4) #  SCL

PIN_D7      = const(5)
PIN_D6      = const(6)
PIN_D5      = const(7)
PIN_D4      = const(8)
PIN_D3      = const(9)
PIN_D2      = const(10)
PIN_D1      = const(11)
PIN_D0      = const(12)
PIN_VSYNC   = const(13)
PIN_HREF    = const(14)
PIN_PCLK    = const(15)

XCLK_MHZ    = const(16)  #  camera machine clock
PIXFORMAT   = const(17)  #  pixel format
FRAMESIZE   = const(18)  #  framesize
JPEG_QUALITY= const(19)
FB_COUNT    = const(20)  #  framebuffer count > 1 continuous mode (JPEG only)

PIXFORMAT_RGB565    = const(1) # 2BPP/RGB565
PIXFORMAT_YUV422    = const(2) # 2BPP/YUV422
PIXFORMAT_YUV420    = const(3) # 1.5BPP/YUV420
PIXFORMAT_GRAYSCALE = const(4) # 1BPP/GRAYSCALE
PIXFORMAT_JPEG      = const(5) # JPEG/COMPRESSED
PIXFORMAT_RGB888    = const(6) # 3BPP/RGB888
PIXFORMAT_RAW       = const(7) # RAW
PIXFORMAT_RGB444    = const(8) # 3BP2P/RGB444
PIXFORMAT_RGB555    = const(9) # 3BP2P/RGB555

FRAMESIZE_96X96   = const(1)  # 96x96 (width x height)
FRAMESIZE_QQVGA   = const(2)  # 160x120
FRAMESIZE_QCIF    = const(3)  # 176x144
FRAMESIZE_HQVGA   = const(4)  # 240x176
FRAMESIZE_240X240 = const(5)  # 240x240
FRAMESIZE_QVGA    = const(6)  # 320x240
FRAMESIZE_CIF     = const(7)  # 400x296
FRAMESIZE_HVGA    = const(8)  # 480x320
FRAMESIZE_VGA     = const(9)  # 640x480
FRAMESIZE_SVGA    = const(10) # 800x600
FRAMESIZE_XGA     = const(11) # 1024x768
FRAMESIZE_HD      = const(12) # 1280x720
FRAMESIZE_SXGA    = const(13) # 1280x1024
FRAMESIZE_UXGA    = const(14) # 1600x1200
FRAMESIZE_FHD     = const(15) # 1920x1080
FRAMESIZE_P_HD    = const(16) # 720x1280
FRAMESIZE_P_3MP   = const(17) # 864x1536
FRAMESIZE_QXGA    = const(18) # 2048x1536

#-------------------------------------------------------------
# OV2640 Boards configuration below (can edit - add your board)

# Freenove esp32s3-cam board (default in firmware)
freenove = {PIN_PWDN:-1,
            PIN_RESET:-1,
            PIN_XCLK:15,
            PIN_SIOD:4,
            PIN_SIOC:5,
            PIN_D7:16,
            PIN_D6:17,
            PIN_D5:18,
            PIN_D4:12,
            PIN_D3:10,
            PIN_D2:8,
            PIN_D1:9,
            PIN_D0:11,
            PIN_VSYNC:6,
            PIN_HREF:7,
            PIN_PCLK:13,
            XCLK_MHZ:14,
            PIXFORMAT:5,
            FRAMESIZE:10,
            JPEG_QUALITY:12,
            FB_COUNT:2, 
}

# add your cam board config below

