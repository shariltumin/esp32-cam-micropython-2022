
Exit 2023, enter 2024. New year, new opportunity. This work is a revision of the Christmas-2023-Edition and completes the task of providing firmwares for esp32s3 as well.

Supported firmwares are:
1. esp32-aiThinker
2. esp32s3-freenove
3. esp32s3-lilygo
4. esp32s3-xiao

All are compiled with esp-idf-4.4.6 and the camera modules are based on the latest esp32 camera component.

All firmware includes these frozen display modules:
1. ssd1306f - OLED Display Module 12864 128x64 Pixel SSD1306.
2. st7735f  - TFT Display 1.8″ 128×160 Pixels ST7735.

The 'f' suffix is to distinguish the frozen modules from the normal flash based modules, should you wish to use one.

I've tested the st7735f with esp32-aiThinker and the ssd1306f with esp32s3-lilygo. All the test scripts are in the "tests" directories of the respective boards. The esp32s3-freenove firmware now includes the esp32s3 sd/mmc sd card driver, which means that the onboard sd card driver is now usable for storing data.

There is now a new way to configure the camera hardware before the camera is initialised. The PIXFORMAT and FRAMESIZE must be set before ```camera.init()```. If you need to change either or both, you need to run ```camera.deinit()``` first.

Under each "tests" directory, I include a "config_test.py" file. You can run this script to find out what combinations of PIXFORMAT/FRAMESIZE are supported, and what the image file sizes are if a combination is valid.

All firmwares come with "scripts" directories that contain the following:
1. auth.py  - the authorization variables
2. cam_config.py - the configuration definitions and the board configuration 
3. streaming_server.py - a simple HTTP image streaming server

The esp32s3-lilygo needs an extra file, "pmu.py", the power management script.

Besides providing TFT and OLED display capabilities, I also include some opencv scripts.
1. client.py
2. face_detection.py
3. hands_detection.py

These scripts are clients of "streaming_server.py". You need to run the opencv scripts on a unix-based PC, and you need Python with opencv-python, czone and all dependencies installed on that PC.

Good luck with your ESP camera projects for 2024.

