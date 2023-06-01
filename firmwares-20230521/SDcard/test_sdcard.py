import machine, uos
from time import sleep

slt = 1 # slot 0 use by flash memory (1: default)
wid = 1 # sdmmc (sdio) - 1 bit at time (default). Either 1 or 4
        # Only Data0, Data1 line is not used, 
        # so that the LED GPIO4 will not blink
frq = 20000000 # defult:20000000
#frq = 10000000 
sd=machine.SDCard(slot=slt, width=wid, freq=frq)

uos.mount(sd, "/sd")

for i in range(100): # 100 frames video
    print(gc.mem_free())
    data = b'sfsdfsdfeqeqw12414asfasf33qrfsafq3r332rfsfsdff3r3232rgsdvdvwr3efes'*500
    if len(data) > 0:
       print('Frame:', i)
       fn = '/sd/pic-%03d.jpg'%i
       f = open(fn, 'wb')
       w=f.write(data)
       print(i,w,len(data))
       f.close()
       del f
    sleep(0.5)

uos.listdir("/sd")
uos.umount("/sd")

