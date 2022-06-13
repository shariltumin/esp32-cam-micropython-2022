
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

# webcam.py MVC - This is the controller C of MVC

from machine import reset
from time import sleep
import usocket as soc
import gc
#
import camera
from wifi import Sta
from help import Setting as cam_setting
import site

auth=site.auth
pwd=site.pwd

def clean_up(cs):
   cs.close() # flash buffer and close socket
   del cs
   gc.collect()

def route(pm):
   cs,rq=pm
   pth='*NOP*'
   rqp = rq.split('/')
   rl=len(rqp)
   if rl==1: # ''
      pth='/';v=0
   elif rl==2: # '/', '/a'
      pth=f'/{rqp[1]}';v=0
   else: # '/a/v' '/a/v/w/....'
      pth=f'/{rqp[1]}'
      if rqp[1]=='login':
         v=rqp[2]
      else:
         try:
            v=int(rqp[2])
         except:
            v=0
            pth='*ERR*'
            print('Not an integer value', rqp[2])
   if pth in site.app:
      #print(pth, site.app[pth])
      site.app[pth](cs,v)
   elif pth=='*NOP*':
      site.NOP(cs)
   else:
      site.ERR(cs)
   clean_up(cs)

def server(pm):
  p=pm[0]
  ss=soc.socket(soc.AF_INET, soc.SOCK_STREAM)
  ss.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)
  sa = ('0.0.0.0', p)
  ss.bind(sa)
  ss.listen(1) # serve 1 client at a time
  print("Start server", p)
  if auth.on:
     print(f"Try - http://{site.server}/login/{auth.pwd}")
  else:
     print(f"Try - http://{site.server}")
  while True:
     ms='';rq=[]
     try:
        cs, ca = ss.accept()
     except:
        pass
     else:
        r=b'';e=''
        try:
           r = cs.recv(1024) 
        except Exception as e:
           print(f"EX:{e}")
           clean_up(cs)
        try:
           ms = r.decode()
           rq = ms.split(' ')
        except Exception as e:
           print(f"RQ:{ms} EX:{e}")
           clean_up(cs)
        else:
           if len(rq)>=2:
              print(ca, rq[:2])
              rv,ph=rq[:2]  # GET /path
              if not auth.on:
                 route((cs, ph))
                 continue
              elif auth.ip==ca[0]: # authenticated client
                 route((cs, ph))
                 continue
              elif ph.find('login/')>=0: # do login
                 site.client=ca[0]
                 route((cs, ph))
                 continue
              else:
                 # Unauthorized otherwise
                 site.NO(cs) 
                 clean_up(cs) 

# wait for camera ready
for i in range(5):
    cam = camera.init()
    print("Camera ready?: ", cam)
    if cam: break
    else: sleep(2)
else:
    print('Timeout')
    reset() 

if cam:
   print("Camera ready")
   # wait for wifi ready
   w = Sta()
   w.connect()
   w.wait()
   for i in range(5):
       if w.wlan.isconnected(): break
       else: print("WIFI not ready. Wait...");sleep(2)
   else:
      print("WIFI not ready. Can't continue!")
      reset()

# set auth
auth.on=True
#auth.on=False  # False: no authentication needed

if auth.on:
   auth.pwd=pwd()
   auth.ip=''
   print(f'PWD: {auth.pwd}')

# set preffered camera setting
camera.framesize(10)     # frame size 800X600 (1.33 espect ratio)
camera.contrast(2)       # increase contrast
camera.speffect(2)       # jpeg grayscale

cam_setting['framesize']=10
cam_setting['contrast']=2
cam_setting['speffect']=2

site.ip=w.wlan.ifconfig()[0]
site.camera=camera

server((80,))  # port 80
reset()


