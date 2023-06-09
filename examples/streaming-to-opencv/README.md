It is simple to stream to a script running opencv-python module cv2 on a Linux (or Linux-like) PC.

Start the webcam script on the esp32cam.

```
>>> import webcam
```
Just remember to enter your WiFi credentials at line 189 of webcam.py:

```
   w = Sta()
   w.connect('YourSSID', 'YourPassword')
```

You can disable login by setting login to false by auth.on=False
With login disabled, you can include 'import webcam' in main.py and the webcam will start automatically at boot time.

Simply run the script 
```
$ python3 video_streaming.py
```
on the Linux PC. All you have to do is change the IP address in the cv2.VideoCapture()

To use the script, you must first install opencv-python.

