**configuration**:

| name        | key | note |
|-------------|-----------|------|
| PIN_PWDN    |  0  | Powerdown, -1 if not used 
| PIN_RESET   |  1  | Reset, -1 if reset will be done by software
| PIN_XCLK    |  2  | Sensor clock input, -1 if external crystal is used
| PIN_SIOD    |  3  | SCCB serial interface data  (I2C SDA)
| PIN_SIOC    |  4  | SCCB serial interface clock (I2C SCL)
| PIN_D7      |  5  | Video port output Y9 (bit#7)
| PIN_D6      |  6  | Video port output Y8 (bit#6)
| PIN_D5      |  7  | Video port output Y7 (bit#5)
| PIN_D4      |  8  | Video port output Y6 (bit#4)
| PIN_D3      |  9  | Video port output Y5 (bit#3)
| PIN_D2      |  10  | Video port output Y4 (bit#2)
| PIN_D1      |  11  | Video port output Y3 (bit#1) 
| PIN_D0      |  12  | Video port output Y2 (bit#0)
| PIN_VSYNC   |  13  | Vertical synchronization output
| PIN_HREF    |  14  | Horizontal reference output
| PIN_PCLK    |  15  | Pixel clock output
| XCLK_MHZ    |  16  |  Sensor clock speed (10, 20)
| PIXFORMAT   |  17  |  See **pixformat**
| FRAMESIZE   |  18  |  See **framesize**
| JPEG_QUALITY|  19  |  Jpeg quality (10, 63)
| FB_COUNT    |  20  |  1 (esp32 2MB PSRAM) or 2 (esp32s3 8MB PSRAM)

**framesize**:

| name        | key | pixel | note |
|-------------|-----|-------|-----|
| FRAMESIZE_96X96 | 1 | 96x96 | Square  |
| FRAMESIZE_QQVGA | 2 | 160x120 |    |
| FRAMESIZE_QCIF  | 3 | 176x144 |    |
| FRAMESIZE_HQVGA | 4 | 240x176 |    |
| FRAMESIZE_240X240 | 5 | 240x240 | Square  |
| FRAMESIZE_QVGA | 6 | 320x240 |    |
| FRAMESIZE_CIF | 7 | 400x296 |    |
| FRAMESIZE_HVGA | 8 | 480x320 |    |
| FRAMESIZE_VGA | 9 | 640x480 |    |
| FRAMESIZE_SVGA | 10 | 800x600 | default   |
| FRAMESIZE_XGA | 11 | 1024x768 |    |
| FRAMESIZE_HD | 12 | 1280x720 |    |
| FRAMESIZE_SXGA | 13 | 1280x1024 |    |
| FRAMESIZE_UXGA | 14 | 1600x1200 |    |
| FRAMESIZE_FHD | 15 | 1920x1080 |    |
| FRAMESIZE_P_HD | 16 | 720x1280 |    |
| FRAMESIZE_P_3MP | 17 | 864x1536 |    |
| FRAMESIZE_QXGA | 18 | 2048x1536 |    |

**pixformat**:

| name        | key | note |
|-------------|-----------|------|
| PIXFORMAT_RGB565 | 1 | 2BPP/RGB565 |
| PIXFORMAT_YUV422 | 2 | 2BPP/YUV422 |
| PIXFORMAT_YUV420 | 3 | 1.5BPP/YUV420 |
| PIXFORMAT_GRAYSCALE | 4 | 1BPP/GRAYSCALE |
| PIXFORMAT_JPEG | 5 | JPEG/COMPRESSED |
| PIXFORMAT_RGB888 | 6 | 3BPP/RGB888 |
| PIXFORMAT_RAW | 7 | RAW |
| PIXFORMAT_RGB444 | 8 | 3BP2P/RGB444 |
| PIXFORMAT_RGB555 | 9 | 3BP2P/RGB555 |

camera methods (listed alfabatically):

| name        | parameter | note |
|-------------|-----------|------|
| aecvalue    | [0, 1200] default 0 | Automatic Exposure Control   |   
|             |                     | Bigger value longer exposure |
| aelevels    | [-2, 2] default 0 | Automatic Exposure Level |  
|             |                   | Bigger value brighter image |
| agcgain     | [0, 30] default 30 | Automatic Gain Control |
|             |                    | Lower value darker image, less artefact |  
| brightness  | [-2, 2] default 0 | Brightness |
|             |                   | Bigger value brighter image |
| capture     |           | Read sensor buffer into memory |
|             |           | The image format and size depend on pixformat and framesize settings|    
| capture_bmp |           | Convert sensor buffer to BMP and read into memory |
|             |           | The size depends on framesize setting |
| capture_jpg |           | Convert sensor buffer to JPG and read into memory |
|             |           | The size depends on framesize setting |
|             |           | Convert only if pixformat is not JPEG |
| conf        | what, value | camera.conf(w,v) see **configuration** |
|             |             | Configuration with camera.conf() must be done before camera.init() |
| contrast    | [-2, 2] default 0| Constrast, 2 highest constrast |
| deinit      |           | Deinitialize camera sensor. Close and disconnect image sensor from the system|
| flip        |           | Flip image vertically |            
| framesize   | [1, 18] default 10 (SVGA) | See **framesize** |
| init        |           | Initialize camera sensor. Open and connect image sensor to the system. The state persist across soft-reboot. Do camera.deinit() before a new camera.init() ( after change configuration for example) |
| mirror      |           | Flip image horizontally |    
| pixformat   | [1, 9] default 5 (JPEG) | See **pixformat** |    
| quality     | [10, 63] default 12 | JPEG quality, highest quality at 10 |
| saturation  | [-2, 2] default 0 | Color saturation, -2 grayscale and 2 highest color saturation.    
| speffect    | [0, 6] default 0 | Special effect: |
|             |                  | 1 - negative    |
|             |                  | 2 - black and white   | 
|             |                  | 3 - reddish   | 
|             |                  | 4 - greenish  |  
|             |                  | 5 - blueish   | 
|             |                  | 6 - retro (brownish)   | 
| whitebalance| [0, 4] default 0 | White balance: |
|             |                  | 1 - sunny   | 
|             |                  | 2 - cloudy  |  
|             |                  | 3 - office  |  
|             |                  | 4 - home   | 

