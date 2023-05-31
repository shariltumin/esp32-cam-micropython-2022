
The script esp32_ble.py implements the BLE class for the Nordic UART service on the ESP32-cam.

Thanks to the original contributor(s) whose name I do not know.

There are a few changes. For event type 3, the oldest message is kept. The current message is dropped if the message slot is not empty. The method get_message() returns the current message and clears the slot. The assumption here is that get_message() is called in a tight loop, much more often than a client sends a message.

You can send text messages to it using Serial Bluetooth Terminal app on an Android phone. I have problems connecting from an old Android 5.1 phone. No problem from a newer phone with Android 10.

The ble_cam.py script is a sample script that uses the esp32_ble.py module. The script will announce its name and ESP32-KAKI5 will be shown as a BLE device that a client can connect to.

Once connected, image (jpg) recording begins, one frame per file, with a 'start' message. A 'stop' message pauses recording until another 'start' message is sent, which resumes recording. A 'bye' message exits the main loop. The program returns to REPL.

There is a guard variable, max_frames, which sets an upper limit on the number of frames to capture.

For autostart, you can add this line to your main.py
```
import ble_cam
```

When you are done capturing images, transfer the SD card to a Linux PC. Do the following to convert the image files to mp4 video.

```
$ df | grep 'media'
/dev/sda1         7708672     18336    7690336   1% /media/sharil/0E0B-1721

$ ffmpeg -framerate 4 -i /media/sharil/0E0B-1721/pic-%04d.jpg video.mp4

$ celluloid video.mp4

```

Use ffmpeg to convert jpg files into an mp4 file. Use celluloid to view the final video file.

Sorry, I have no tips if you are on Windows or Mac. Maybe you can convert of your old Windows laptop into a Linux PC?

Images out from the camera sensor are in jpeg format. There no support for avi or mp4 format. It is tempting to capture images and save all into a single file, for example video.avi, will will not work, as far as I know.

By the way, you can put a 5 minute sleep in the while loop. Turn off your BLE client, you will still be capturing frames, now every 5 minutes.

Later, you can reconnect and send stop and bye.
