
import camera
import time
import gc

gc.enable()

pix = const(17)
frame = const(18)

# PIXEL FORMAT
PIXFORMAT = {
    'RGB565':1,    # 2BPP/RGB565
    'YUV422':2,    # 2BPP/YUV422
    'YUV420':3,    # 1.5BPP/YUV420
    'GRAYSCALE':4, # 1BPP/GRAYSCALE
    'JPEG':5,      # JPEG/COMPRESSED
    'RGB888':6,    # 3BPP/RGB888
    'RAW':7,       # RAW
    'RGB444':8,    # 3BP2P/RGB444
    'RGB555':9,    # 3BP2P/RGB555
}

# FRAME SIZE 
FRAMESIZE = {
     '96X96':1,  # 96x96
     'QQVGA':2,  # 160x120
     'QCIF':3,   # 176x144
     'HQVGA':4,  # 240x176
     '240X240':5,# 240x240
     'QVGA':6,   # 320x240
     'CIF':7,    # 400x296
     'HVGA':8,   # 480x320
     'VGA':9,    # 640x480
     'SVGA':10,  # 800x600
     'XGA':11,   # 1024x768
     'HD':12,    # 1280x720
     'SXGA':13,  # 1280x1024
     'UXGA':14,  # 1600x1200
     'FHD':15,   # 1920x1080
     'P_HD':16,  # 720x1280
     'P_3MP':17, # 864x1536
     'QXGA':18,  # 2048x1536
}

camera.init()

for p in (
    'RGB565',    # 2BPP/RGB565
    'YUV422',    # 2BPP/YUV422
    'YUV420',    # 1.5BPP/YUV420
    'GRAYSCALE', # 1BPP/GRAYSCALE
    'JPEG',      # JPEG/COMPRESSED
    'RGB888',    # 3BPP/RGB888
    'RAW',       # RAW
    'RGB444',    # 3BP2P/RGB444
    'RGB555'):   # 3BP2P/RGB555
    n = PIXFORMAT.get(p)
    for f in (
     '96X96',  # 96x96
     'QQVGA',  # 160x120
     'QCIF',   # 176x144
     'HQVGA',  # 240x176
     '240X240',# 240x240
     'QVGA',   # 320x240
     'CIF',    # 400x296
     'HVGA',   # 480x320
     'VGA',    # 640x480
     'SVGA',  # 800x600
     'XGA',   # 1024x768
     'HD',    # 1280x720
     'SXGA',  # 1280x1024
     'UXGA',  # 1600x1200
     'FHD',   # 1920x1080
     'P_HD',  # 720x1280
     'P_3MP', # 864x1536
     'QXGA'): # 2048x1536
        s = FRAMESIZE.get(f)
        camera.deinit()
        time.sleep(1)
        gc.collect()
        print('Set', p, f, ':')
        camera.conf(pix, n)  # set pixelformat
        camera.conf(frame, s)# set framesize
        try:
           ok = camera.init()
           if not ok:
              print('Camera initialization fail')
              break
           time.sleep(1)
           img = camera.capture()
           if img:
              print('---> Image size:', len(img))
           else:
              print('No image captured')
        except Exception as e:
           print('ERR:', e)
