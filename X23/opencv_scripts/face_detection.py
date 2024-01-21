
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

# run this on Linux PC with opencv-python module

import cv2

dropped = 0 # drop frames count
from cvzone import FaceDetectionModule

face = FaceDetectionModule.FaceDetector()

# Change this to your board IP
# url = 'http://192.168.4.74/free/Hi-Nove-La'a # freenove
# url = 'http://192.168.4.70/xiao/Hi-Xiao-Ling' # xio
# url = 'http://192.168.4.71/lily/Hi-Lily-Goen' # lilygo
url = 'http://192.168.4.97/ait/Hi-AIT-123' # esp32 AiThinker

vid = cv2.VideoCapture(url) # open webcam capture, http-based streaming. Not RTSP

while True:
    ret, frame = vid.read() # get frame-by-frame
    #print(vid.isOpened(), ret)
    if frame is not None:
        if dropped > 0: dropped = 0 # reset
        frame, faces = face.findFaces(frame)
        # if faces:
        #    do other face processing
        cv2.imshow('Faces',frame) # display frame
        if cv2.waitKey(22) & 0xFF == ord('q'): # press q to quit
            break
    else:
        dropped += 1
        if dropped > 100:
           print("Server is down")
           break

# Done, clear all resources
vid.release()
cv2.destroyAllWindows()
print("Video stop")


