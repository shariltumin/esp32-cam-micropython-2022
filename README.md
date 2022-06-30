
# esp32-cam-micropython-2022


![esp32-cam](IMG_20220613_231019-01.jpeg)

It was three years ago. I started playing with MicroPython with camera support on an ESP32-Camera board with MicroPython version 1.11-XXX.


This time, the firmware support version 1.18-XXX. We may reach version 2.00-XXX by the end of 2022. The MicroPython team has been busy.


The build process and structure have changed since version 1.11-XXX.


This firmware is made especially for the ESP32-Camera board and was cleanly compiled with Espressif IDF version 4.4. It supports the OV2640 camera and PSRAM. To reduce size, webrepl, BLE, help modules were not included in the firmware.


I wish to reach a wider audience. So, I will try to make this as simple as possible. To join the fun, these are what you need to do:

 1. Download MicroPython firmware file firmware.bin
 2. Download script files help.py,  html.py,  site.py,  webcam.py, and  wifi.py
 3. Flash the firmware.bin to your ESP32-Camera board
 4. Save the five script files onto the flash file system of your ESP32-Camera board.
 5. Install *thonny* Python IDE from https://thonny.org

The *thonny* IDE helps beginners flash new firmware and upload script files to a development board.


To flash a new MicroPython firmware, these are what you need to:

 1. Connect GPIO-00 and GND pins. 
 2. Connect your ESP32-Camera board to an FTDI USB UART adapter. Remember to cross TX and RX wires between the board and adapter.
 3. Connect the FTDI adapter to a USB port of your PC.
 4. Start *thonny* IDE
 5. Click Tools --> Options --> Interpreter, choose MicroPython (ESP32). For Port, choose "Try to detect port automatically"
 6. Click the "Install or update firmware" link. Click Reload and choose Port value, for example /dev/ttyUSB0". Click [Browse...] and choose the firmware file. Click Install. Click Close when Done!
 7. Remove the wire between GPIO-00 and GND pins and push the RST button on the development board.

Hopefully, you will get MicroPython REPL in the thonny IDE shell window.


```python
MicroPython v1.18-610-gcf7d962cf-kaki5 on 2022-06-10; ESP32 CAMERA module (KAKI5) with ESP32

>>> 
```

We can test the camera module in the REPL

```python
>>> import camera

>>> camera.init()

True

>>> img=camera.capture()

>>> len(img)

58810

>>>
```


Congratulation. We now have a working MicroPython with the camera module.


We will now upload the five script files onto the flash file system using thonny IDE. Click [Open...] to load each script file into the IDE. You should have all five files in different TAB windows. You need to edit the 'wifi.py' file. Change the "YOUR-SSID" and "YOUR-PWD" to the values of your home WiFi.

Save all the five files to "MicroPython device". Do this for each script file. Click File --> Save as... and choose MicroPython device as destination. Make sure to write the correct file name.


We can check whether all five files are in the flash storage using the REPL.


```python
>>> uos.listdir()

['boot.py', 'help.py', 'html.py', 'site.py', 'webcam.py', 'wifi.py']

>>>
```


We are now ready to try our webcam server. In the REPL:

```python
>>> execfile('webcam.py')

Camera ready?:  True

Camera ready

Waiting ...

Waiting ...

Connected to dlink-3530

network config: ('10.0.0.46', '255.255.255.0', '10.0.0.138', '148.122.164.253')

PWD: M1XDYKh3

Start server 80

Try - http://10.0.0.46/login/M1XDYKh3
```


Your output will differ from what is shown here. Open a browser and go to the login URL. You will get "OK!" if successful. Now, go to the 'root' page, for example, http://10.0.0.46. You will receive a 'help' page.


Once login, the server is locked to the IP of the PC. Requests from other PCs are not allowed. To remove the lock, you need to logout, for example, http://10.0.0.46/logout. The server will create a new random login password. You will see the new password in the REPL.


```python
('10.0.0.72', 37146) ['GET', '/logout']

New PWD: IT0XfQOQ
```


You need to use the new password to login again. You can disable the authentication scheme by 'auth.on=False' in webcam.py.


After login, you can try:

 1. Rotate the image in the browser. http://10.0.0.46/rot/90
 2. Take a photo and show it in the browser. http://10.0.0.46/snap
 3. Live streaming to the browser. http://10.0.0.46/webcam
 4. Get help page. http://10.0.0.46

Please change the IP to your server IP. For more information, please read the help page.

Our *webcam* server provides us with microservices to control the camera and
capture images. This means, on a linux PC, we can use *wget* or *curl* to request a service.

It is super easy to make timelapse video on a linux PC:

 1. login
```bash
wget http://10.0.0.46/login/M1XDYKh3
```
-OR-
```bash
curl http://10.0.0.46/login/M1XDYKh3
```
 2. get a still photo
```bash
wget http://10.0.0.46/foto -o foto1.jpeg
```
-OR-
```bash
curl http://10.0.0.46/foto --output foto2.jpeg
```
 3. a simple loop in a bash script will take an image every 30sec
```bash
#!/bin/bash

cnt=0
while :
do
  let "cnt=cnt+1"
  N=$( printf '%04d' $cnt )
  curl http://10.0.0.87/foto --output foto$N.jpeg
  sleep 30
done
```
 4. run the *get_foto.sh* script
```bash
/get_foto.sh 2>/dev/null &
[1] 34394
```
 5. kill it whenever you are done
```bash
kill -9 34394

[1]+  Killed                  ./get_foto.sh 2> /dev/null
```
 6. rotate the photos if needed using *convert* in a script *rot_foto.sh*, try different rotate value (-90, 90)
```bash
#!/bin/bash

for f in `ls foto*.jpeg`
do
 echo "Rotate $f"
 convert $f -rotate 90 $f
done
```
 7. from foto\*.jpeg make timelapse tmlap.mp4 using *ffmpeg*
```bash
cat foto*.jpeg | ffmpeg -f image2pipe -r 1 -vcodec mjpeg -i - -vcodec libx264 tmlap.mp4
```
 8. you can use *curl* to record live video too
```bash
curl http://10.0.0.87/live --output live.avi
<ctrl>+c to kill curl
```
 9. use *celluloid* to show the videos
```bash
celluloid tmlap.mp4

celluloid live.avi
```

You can now live stream video from your ESP32-Camera board at your front gate.

You can also do other projects with your ESP32-Camera board now that you have camera-enabled MicroPython firmware. 

Good luck.

