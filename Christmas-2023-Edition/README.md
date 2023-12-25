
It is Christmas 2023. Since everyone is on holiday and has time on their hands, why not make the most of it? Ok, I have a present for you all.

I have made new esp32 camera firmwares with bug fixes of the old ones. With the new firmwares you can set PIXFORMAT correctly to RGB565, a 2bytes/pixel image format. The 2Bytes with 5bits for red, 6bits for green and 5bits for blue can be used directly on TFT (Thin Film Transistor Liquid Crystal) displays such as ST7735, and ST7789. There is no need for a conversion program, just capture an image and send it directly to the display.

The old firmwares work for JPEG, but setting to a different PIXFORMAT either results in an error or the camera sensor retains the previous JPEG format. The esp-camera ESP-IDF component used in these firmwares behaves differently to the one used before. PIXFORMAT and FRAMESIZE must be set before camera.init(). If you want to change either PIXFORMAT or FRAMESIZE after the camera has been initialised, you must call camera.deinit() first. Any changes will take effect on the next camera.init().

The camera.init() and camera.deinit() will return True if everything went fine. Something is wrong if you get False. The only way to fix this is a hard reset(off/on) or machine.reset().

The camera.init() in the new firmwares will not set any defaults as before, you will need to configure the camera sensor board using the cam_config MicroPython module, for example:

```py
import camera
import cam_config as cc
# set camera configuration
cc.configure(camera, cc.ai_thinker)
camera.init()
```

The cc.ai_thinker is a dict that contains all the pins and default configuration settings. This provides flexibility. Users can adjust the settings according to their OV2640 boards. For example, if you are using the external "Red Board" and you are using the settings in "cam_config.py", you can just do ```cc.configure(camera, cc.red_board)```.

These firmwares only support the OV2640 camera sensor. By using "cam_config.py" it is possible to use any OV2640 board. You will need to set the pins correctly.

I have tested the esp32-cam (ai-thinker) board and ST7735. I got good results. You can find the test codes in the scripts directory.

Best of luck and Happy New Year, 2024.


