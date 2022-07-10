
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

# html.py  MVC - This is the view V of MVC

pg = {
  # URL: /webcam -> /live, /snap -> /foto, /blitz -> /boto
  'foto':'''<!DOCTYPE html>
<html>
<head>
<title>ESP32 Camera</title>
<link rel="icon" href="data:image/gif;base64,R0lGODlhAQABAAAAACwAAAAAAQABAAA=">
</head>
<body>
  <div style="display:flex;  margin-top: 15%%; justify-content:center; align-items:center; height:600px;">
    <img src="%s" style="height:100%%; transform:rotate(%sdeg);"/>
  </div>
</body>
</html>
''',
  'favicon':'''<!DOCTYPE html>
<html>
<head>
<link rel="icon" href="data:image/gif;base64,R0lGODlhAQABAAAAACwAAAAAAQABAAA=">
</head>
<body>
</body>
</html>
''',
  'err':'''Sorry, I can not do that.
''',
  'none':'''Sorry, nothing there.
''',
  'no': '''Sorry, unauthorized.
''',
  'OK':'''OK!
''',
}

hdr = {
  # start page for streaming
  # URL: /webcam, /snap, /blitz
  'foto': """HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Connection: Closed
Content-Length: %d""",
  # live stream -
  # URL: /live
  'stream': """HTTP/1.1 200 OK
Content-Type: multipart/x-mixed-replace; boundary=frame
Connection: keep-alive
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Expires: Thu, Jan 01 1970 00:00:00 GMT
Pragma: no-cache""",
  # live stream -
  # URL:
  'frame': """--frame
Content-Type: image/jpeg""",
  # still picture -
  # URL: /foto
  'pix': """HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: %d""",
  #
  'pic': """HTTP/1.1 200 OK
Content-Type: image/jpeg""",
  # no content error
  # URL: all the rest
  'none': """HTTP/1.1 400 Bad Request
Content-Type: text/plain; charset=utf-8
Connection: Closed
Content-Length: %d""",
  # URL: /favicon.ico
  'favicon': """HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Connection: Closed
Cache-Control: max-age=2592000, public
Content-Length: %d""",
  # bad request error
  # URL: all the rest
  'err': """HTTP/1.1 400 Bad Request
Content-Type: text/plain; charset=utf-8
Connection: Closed
Content-Length: %d""",
  # OK
  # URL: all the rest
  'OK': """HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8
Connection: Closed
Content-Length: %d""",
  # NO
  # URL: not authenticated
  'NO': """HTTP/1.1 401	Unauthorized
Content-Type: text/plain; charset=utf-8
Connection: Closed
Content-Length: %d""",
}

