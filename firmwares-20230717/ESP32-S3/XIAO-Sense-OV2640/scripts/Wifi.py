
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

#Basic WiFi configuration:

from time import sleep
import network

class Sta:

   AP = "dlink-2391"  # change to your SSID
   PWD = "f34RT114k"  # cjange to your password

   def __init__(my, ap='', pwd=''):
      network.WLAN(network.AP_IF).active(False) # disable access point
      my.wlan = network.WLAN(network.STA_IF)
      my.wlan.active(True)
      if ap == '':
        my.ap = Sta.AP
        my.pwd = Sta.PWD 
      else:
        my.ap = ap
        my.pwd = pwd

   def connect(my, ap='', pwd=''):
      if ap != '':
        my.ap = ap
        my.pwd = pwd

      if not my.wlan.isconnected(): 
        my.wlan.connect(my.ap, my.pwd)

   def status(my):
      if my.wlan.isconnected():
        return my.wlan.ifconfig()
      else:
        return ()

   def wait(my):
      cnt = 30
      while cnt > 0:
         print("Waiting ..." )
         # con(my.ap, my.pwd) # Connect to an AP
         if my.wlan.isconnected():
           print("Connected to %s" % my.ap)
           print('network config:', my.wlan.ifconfig())
           cnt = 0
         else:
           sleep(5)
           cnt -= 5
      return

   def scan(my):
      return my.wlan.scan()   # Scan for available access points

