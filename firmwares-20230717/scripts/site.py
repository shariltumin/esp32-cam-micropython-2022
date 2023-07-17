
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

# site.py MVC - This is the model M of MVC

from uos import urandom as ran
from machine import Pin
from html import pg, hdr
from help import Setting as cam
from help import help

# Init global variables
rot='0'
flash_light=Pin(04,Pin.OUT)

class auth: pass

server=''
client=''

def pwd(size=8):
    alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    return ''.join([alfa[x] for x in [(ran(1)[0] % len(alfa)) for _ in range(size)]])

# These will be set by server script as site.ip and site.camera
ip=''
camera=None  

app={}
def route(p):
    def w(g):
        app[p]=g
    return w

def OK(cs):
   p=pg['OK']
   ln=len(p)+2
   cs.write(b'%s\r\n\r\n%s\r\n' % (hdr['OK']%ln, p))

def ERR(cs):
   p=pg['err']
   ln=len(p)+2
   cs.write(b'%s\r\n\r\n%s\r\n' % (hdr['err']%ln, p))

def NO(cs):
   p=pg['no']
   ln=len(p)+2
   cs.write(b'%s\r\n\r\n%s\r\n' % (hdr['err']%ln, p))

def NOP(cs):
   p=pg['none']
   ln=len(p)+2
   cs.write(b'%s\r\n\r\n%s\r\n' % (hdr['none']%ln, p))

def setting(cs,w,ok,cmd,v):
   #print("setting:", w, ok)
   if ok:
      cmd(w); cam[v]=w
      OK(cs)
   else:
      ERR(cs)

@route('/')
def root(cs,v):
   p=help(server)
   ln=len(p)+2
   cs.write(b'%s\r\n\r\n%s\r\n' % (hdr['OK']%ln, p))
   OK(cs)

@route('/login')
def login(cs,v):
   if auth.on:
      if auth.ip=='':
         if v==auth.pwd:
            auth.ip=client
   OK(cs)

@route('/logout')
def logout(cs,v):
   if auth.on:
      auth.pwd=pwd()
      auth.ip=''
      print(f'New PWD: {auth.pwd}')
   OK(cs)

@route('/favicon.ico')
def fav(cs,v):
    p=pg['favicon']
    ln=len(p)+2
    cs.write(b'%s\r\n\r\n%s\r\n' % (hdr['favicon']%ln, p))

@route('/webcam')
def webcam(cs,v):
    global ip,rot
    p=pg['foto']%(f'http://{ip}/live',rot) # needed by opera, vivaldi, midori..
    ln=len(p)+2
    cs.write(b'%s\r\n\r\n%s\r\n' % (hdr['foto']%ln, p))

@route('/live')
def live(cs,v): # live stream
    cs.write(b'%s\r\n\r\n' % hdr['stream'])
    cs.setblocking(True)
    pic=camera.capture
    put=cs.write
    hr=hdr['frame']
    while True:
       try:
          put(b'%s\r\n\r\n' % hr)
          put(pic())
          put(b'\r\n')  # send and flush the send buffer
       except Exception as e:
          print(e)
          break

@route('/snap')
def snap(cs,v):
    global ip,rot
    p=pg['foto']%(f'http://{ip}/foto',rot)
    ln=len(p)+2
    cs.write(b'%s\r\n\r\n%s\r\n' % (hdr['foto']%ln, p))

@route('/blitz')
def blitz(cs,v):
    global ip,rot
    p=pg['foto']%(f'http://{ip}/boto',rot)
    ln=len(p)+2
    cs.write(b'%s\r\n\r\n%s\r\n' % (hdr['foto']%ln, p))

@route('/foto')
def foto(cs,v): # still photo
    #buf=camera.capture()
    #ln=len(buf)
    cs.setblocking(True)
    cs.write(b'%s\r\n\r\n' % hdr['pic'])
    cs.write(camera.capture())
    cs.write(b'\r\n')  # send and flush the send buffer
    #nc=cs.write(b'%s\r\n\r\n' % (hdr['pix']%ln)+buf)

@route('/boto')
def boto(cs,v): # still photo blitz on
    #buf=camera.capture()
    #ln=len(buf)
    cs.setblocking(True)
    cs.write(b'%s\r\n\r\n' % hdr['pic'])
    flash_light.on()
    cs.write(camera.capture())
    flash_light.off()
    cs.write(b'\r\n')
    #nc=cs.write(b'%s\r\n\r\n' % (hdr['pix']%ln)+buf)

@route('/rot')
def rotate(cs,v):
    global rot
    rot=v
    OK(cs)

@route('/flash')
def flash(cs,v):
    if v==1: flash_light.on()
    else: flash_light.off()
    OK(cs)

@route('/fmt')
def fmt(cs,w): 
    setting(cs,w,(w>=1 and w<=9),camera.pixformat,'pixformat')

@route('/pix')
def pix(cs,w): 
    setting(cs,w,(w>0 and w<18),camera.framesize,'framesize')

@route('/qua')
def qua(cs,w): 
    setting(cs,w,(w>9 and w<64),camera.quality,'quality')

@route('/con')
def con(cs,w): 
    setting(cs,w,(w>-3 and w<3),camera.contrast,'contrast')

@route('/sat')
def sat(cs,w): 
    setting(cs,w,(w>-3 and w<3),camera.saturation,'saturation')

@route('/bri')
def bri(cs,w): 
    setting(cs,w,(w>-3 and w<3),camera.brightness,'brightness')

@route('/ael')
def ael(cs,w): 
    setting(cs,w,(w>-3 and w<3),camera.aelevels,'aelevels')

@route('/aec')
def aec(cs,w): 
    setting(cs,w,(w>=0 and w<=1200),camera.aecvalue,'aecvalue')

@route('/agc')
def agc(cs,w): 
    setting(cs,w,(w>=0 and w<=30),camera.agcgain,'agcgain')

@route('/spe')
def spe(cs,w): 
    setting(cs,w,(w>=0 and w<7),camera.speffect,'speffect')

@route('/wbl')
def wbl(cs,w): 
    setting(cs,w,(w>=0 and w<5),camera.whitebalance,'whitebalance')


