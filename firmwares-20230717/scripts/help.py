
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
#

Setting = {
    'pixformat':5,  # 1:RGB565, 2:YUV422, 3:YUV420, 4:GRAYSCALE, 5:COMPRESSED, 
                    # 6:RGB888, 7:RAW, 8:RGB444, 9:RGB555
    'framesize':11, # 1:96x96, 2:160x120, 3:176x144, 4:240x176, 5:240x240
                    # 6:320x240, 7:400x296, 8:480x320, 9:640x480, 10:800x600
                    # 11:1024x768, 12:1280x720, 13:1280x1024, 14:1600x1200
                    # 15:1920x1080, 16:720x1280, 17:864x1536, 18:2048x1536

    'quality':11,   # [0,63] lower number means higher quality
    'contrast':0,   # [-2,2] higher number higher contrast
    'saturation':0, # [-2,2] higher number higher saturation. -2 grayscale
    'brightness':0, # [-2,2] higher number higher brightness. 2 brightest
    'speffect':0,   # 0:,no effect 1:negative, 2:black and white, 3:reddish, 
                    # 4:greenish, 5:blue, 6:retro

    'whitebalance':0, # 0:default, 1:sunny, 2:cloudy, 3:office, 4:home
    'aelevels':0,     # [-2,2] AE Level: Automatic exposure
    'aecvalue':0,     # [0,1200] AEC Value: Automatic exposure control
    'agcgain':0,      # [0,30] AGC Gain: Automatic Gain Control
}

def help(server):
    c=Setting
    return f"""
Autentication:
  Login to server with a one-time password.
  http://{server}/login/<PWD>
  After login, only the authenticated client can connect to server.

  Logout from server.
  http://{server}/logout
  The client is no longer authenticated. Create new one-time password.
  The password is shown in REPL.
  Any web browser can now login using the password.

  NB! The server is open to all if auth.on=False

Help:
  Show this page
  http://{server}
  If auth.on=True then you need to login first.

Streaming:
  Webcam live streaming
  http://{server}/webcam
  To stop streaming just go to other URL e.g. http://{server}/snap

Still photo:
  Take picture
  http://{server}/snap

  Take picture with LED flash
  http://{server}/blitz

HTML image view port rotation:
  Rotate the <img> with transform:rotate() in style defination.
  http://{server}/rot/n
  n is one these value [0,90,180,270,360]. You can display the 
  image/video taken by the camera in portrait or landscape mode by
  rotating the image view port. Depending on your camera sensor and
  the orientation of your board, http://{server}/rot/90 may show
  portrait mode image on your browser.

Camera setting:
  pixformat - http://{server}/fmt/n
  framesize - http://{server}/pix/n
  quality - http://{server}/qua/n
  contrast - http://{server}/con/n
  saturation - http://{server}/sat/n
  brightness - http://{server}/bri/n
  speffect - http://{server}/spe/n
  whitebalance - http://{server}/wbl/n
  aelevels - http://{server}/ael/n
  aecvalue - http://{server}/aec/n
  agcgain - http://{server}/agc/n

  NB! n is integer value (can be negative). 
      See listing below for appropriate value for each setting.

Camera current setting:
  pixformat={c['pixformat']}  # 1:2BPP/RGB565, 2:2BPP/YUV422, 3:1.5BPP/YUV420, 
                              # 4:1BPP/GRAYSCALE, 5:JPEG/COMPRESSED, 6:3BPP/RGB888, 
                              # 7:RAW, 8:3BP2P/RGB444, 9:3BP2P/RGB555
  framesize={c['framesize']}   # 1:96x96, 2:160x120, 3:176x144, 4:240x176, 5:240x240
                 # 6:320x240, 7:400x296, 8:480x320, 9:640x480, 10:800x600
                 # 11:1024x768, 12:1280x720, 13:1280x1024, 14:1600x1200
                 # 15:1920x1080, 16:720x1280, 17:864x1536, 18:2048x1536
  quality={c['quality']}     # [10,63] lower number means higher quality
  contrast={c['contrast']}     # [-2,2] higher number higher contrast
  saturation={c['saturation']}   # [-2,2] higher number higher saturation. -2 grayscale
  brightness={c['brightness']}   # [-2,2] higher number higher brightness. 2 brightest
  speffect={c['speffect']}     # 0:,no effect 1:negative, 2:black and white, 3:reddish, 
                 # 4:greenish, 5:blue, 6:retro
  whitebalance={c['whitebalance']} # 0:default, 1:sunny, 2:cloudy, 3:office, 4:home
  aelevels={c['aelevels']}     # [-2,2] AE Level: Automatic exposure
  aecvalue={c['aecvalue']}     # [0,1200] AEC Value: Automatic exposure control
  agcgain={c['agcgain']}      # [0,30] AGC Gain: Automatic Gain Control

"""

