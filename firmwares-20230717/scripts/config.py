
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

#-------------------------------------------------------------

# OV2640 Boards configuration below (can edit - add your board)

# AI-Thinker esp32-cam board
ai_thinker = {PIN_PWDN:32,
              PIN_RESET:-1,
              PIN_XCLK:0,
              PIN_SIOD:26,
              PIN_SIOC:27,
              PIN_D7:35,
              PIN_D6:34,
              PIN_D5:39,
              PIN_D4:36,
              PIN_D3:21,
              PIN_D2:19,
              PIN_D1:18,
              PIN_D0:5,
              PIN_VSYNC:25,
              PIN_HREF:23,
              PIN_PCLK:22,
              XCLK_MHZ:16,
              PIXFORMAT:5,
              FRAMESIZE:10,
              JPEG_QUALITY:10,
              FB_COUNT:1, 
}

# New 2022 esp32vrover dev
esp_eye =    {PIN_PWDN:-1,
              PIN_RESET:-1,
              PIN_XCLK:4,
              PIN_SIOD:18,
              PIN_SIOC:23,
              PIN_D7:36,
              PIN_D6:37,
              PIN_D5:38,
              PIN_D4:39,
              PIN_D3:35,
              PIN_D2:14,
              PIN_D1:13,
              PIN_D0:34,
              PIN_VSYNC:5,
              PIN_HREF:27,
              PIN_PCLK:25,
              XCLK_MHZ:16,
              PIXFORMAT:5,
              FRAMESIZE:10,
              JPEG_QUALITY:10,
              FB_COUNT:1,
}

# esp32 wrover dev 
wrover_dev = {PIN_PWDN:32,
              PIN_RESET:-1,
              PIN_XCLK:21,
              PIN_SIOD:26,
              PIN_SIOC:27,
              PIN_D7:35,
              PIN_D6:34,
              PIN_D5:39,
              PIN_D4:36,
              PIN_D3:19,
              PIN_D2:18,
              PIN_D1:5,
              PIN_D0:4,
              PIN_VSYNC:25,
              PIN_HREF:23,
              PIN_PCLK:22,
              XCLK_MHZ:12,
              PIXFORMAT:5,
              FRAMESIZE:10,
              JPEG_QUALITY:10,
              FB_COUNT:1,
}

# Test 
wrover_test = {PIN_PWDN:-1,
              PIN_RESET:-1,
              PIN_XCLK:21,
              PIN_SIOD:26,
              PIN_SIOC:27,
              PIN_D7:35,
              PIN_D6:34,
              PIN_D5:39,
              PIN_D4:36,
              PIN_D3:19,
              PIN_D2:18,
              PIN_D1:5,
              PIN_D0:4,
              PIN_VSYNC:25,
              PIN_HREF:23,
              PIN_PCLK:22,
              XCLK_MHZ:12,
              PIXFORMAT:5,
              FRAMESIZE:10,
              JPEG_QUALITY:10,
              FB_COUNT:1,
}

# Red Board (has internal clock for camera set at 12Mhz)
red_board =  {PIN_PWDN:32, # 
              PIN_RESET:-1,
              PIN_XCLK:-1, # internal sensor clock
              PIN_SIOD:26,
              PIN_SIOC:27,
              PIN_D7:35,
              PIN_D6:34,
              PIN_D5:39,
              PIN_D4:36,
              PIN_D3:21, 
              PIN_D2:19, 
              PIN_D1:18, 
              PIN_D0:5,  
              PIN_VSYNC:25,
              PIN_HREF:23,
              PIN_PCLK:22,
              XCLK_MHZ:12, # the board has 12Mhz intrenal clock (MUST set to 12)
              PIXFORMAT:5,
              FRAMESIZE:10,
              JPEG_QUALITY:10,
              FB_COUNT:1,
}

# XIAO ESP32S3 Sense Camera
xiao_s3_sense =  {PIN_PWDN:-1, 
              PIN_RESET:-1,
              PIN_XCLK:10, 
              PIN_SIOD:40,
              PIN_SIOC:39,
              PIN_D7:48,
              PIN_D6:11,
              PIN_D5:12,
              PIN_D4:14,
              PIN_D3:16,
              PIN_D2:18,
              PIN_D1:17,
              PIN_D0:15,
              PIN_VSYNC:38,
              PIN_HREF:47,
              PIN_PCLK:13,
              XCLK_MHZ:14, 
              PIXFORMAT:5,
              FRAMESIZE:10,
              JPEG_QUALITY:12,
              FB_COUNT:1,
}

# LILYGO T-Camera esp32s3 V1.6
lilygo_t_camera =  {PIN_PWDN:-1, 
              PIN_RESET:39,
              PIN_XCLK:38, 
              PIN_SIOD:5,
              PIN_SIOC:4,
              PIN_D7:9,
              PIN_D6:10,
              PIN_D5:11,
              PIN_D4:13,
              PIN_D3:21,
              PIN_D2:48,
              PIN_D1:47,
              PIN_D0:14,
              PIN_VSYNC:8,
              PIN_HREF:18,
              PIN_PCLK:12,
              XCLK_MHZ:14,
              PIXFORMAT:5,
              FRAMESIZE:10,
              JPEG_QUALITY:12,
              FB_COUNT:2,
}

# FREENOVE esp32s3 WROOM FNK0085 A1B0
freenove_fnk0085 =  {PIN_PWDN:-1, 
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

def configure(cam, config):
    for key, val in config.items():
        # print(key, val)
        cam.conf(key, val)

