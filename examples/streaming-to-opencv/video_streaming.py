import cv2

dropped = 0 # drop frames count

vid = cv2.VideoCapture('http://10.0.4.44/live') # open webcam capture

while True:
    ret, frame = vid.read() # get frame-by-frame
    #print(vid.isOpened(), ret)
    if frame is not None:
        if dropped > 0: dropped = 0 # reset
        cv2.imshow('Video-44',frame) # display frame
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


