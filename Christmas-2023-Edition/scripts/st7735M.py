_E='Height'
_D='Width'
_C=True
_B=None
_A=False
import machine,time
from math import sqrt
TFTRotations=[0,96,192,160]
TFTBGR=8
TFTRGB=0
@micropython.native
def clamp(aValue,aMin,aMax):return max(aMin,min(aMax,aValue))
@micropython.native
def TFTColor(aR,aG,aB):'Create a 16 bit rgb value from the given R,G,B from 0-255.\n     This assumes rgb 565 layout and will be incorrect for bgr.';return(aR&248)<<8|(aG&252)<<3|aB>>3
class TFT:
	' define different model of ST7735, circuit board color or types (tabcolor).';GREENTAB=0;REDTAB=1;BLACKTAB=2;GREENTAB2=3;GREENTAB3=4;GREENTAB128x128=5;GREENTAB80x160=6;REDTAB80x160=7;BLUETAB=11;NOP=0;SWRESET=1;RDDID=4;RDDST=9;SLPIN=16;SLPOUT=17;PTLON=18;NORON=19;INVOFF=32;INVON=33;DISPOFF=40;DISPON=41;CASET=42;RASET=43;RAMWR=44;RAMRD=46;COLMOD=58;MADCTL=54;FRMCTR1=177;FRMCTR2=178;FRMCTR3=179;INVCTR=180;DISSET5=182;PWCTR1=192;PWCTR2=193;PWCTR3=194;PWCTR4=195;PWCTR5=196;VMCTR1=197;RDID1=218;RDID2=219;RDID3=220;RDID4=221;PWCTR6=252;GMCTRP1=224;GMCTRN1=225;BLACK=0;RED=TFTColor(255,0,0);MAROON=TFTColor(128,0,0);GREEN=TFTColor(0,255,0);FOREST=TFTColor(0,128,128);BLUE=TFTColor(0,0,255);NAVY=TFTColor(0,0,128);CYAN=TFTColor(0,255,255);YELLOW=TFTColor(255,255,0);PURPLE=TFTColor(255,0,255);WHITE=TFTColor(255,255,255);GRAY=TFTColor(128,128,128)
	@staticmethod
	def color(aR,aG,aB):'Create a 565 rgb TFTColor value';return TFTColor(aR,aG,aB)
	def __init__(A,spi,aDC,aReset=_B,aCS=_B):
		"aLoc SPI pin location is either 1 for 'X' or 2 for 'Y'.\n       aDC is the DC pin and aReset is the reset pin.";B=aReset;A.tabcolor=0;A._size=128,128;A.rotate=2;A._offset=2,3;A._rgb=_A;A.dc=machine.Pin(aDC,machine.Pin.OUT)
		if B==_B:A.useReset=_A
		else:A.useReset=_C;A.reset=machine.Pin(B,machine.Pin.OUT)
		if aCS==_B:A.useCS=_A
		else:A.useCS=_C;A.csPin=machine.Pin(aCS,machine.Pin.OUT)
		A.cs(1);A.spi=spi;A.colorData=bytearray(2);A.windowLocData=bytearray(4)
	def cs(A,iologic):
		if A.useCS:A.csPin(iologic)
	def size(A):return A._size
	def offset(A):return A._offset
	@micropython.native
	def on(self,aTF=_C):'Turn display on or off.';self._writecommand(TFT.DISPON if aTF else TFT.DISPOFF)
	@micropython.native
	def invertcolor(self,aBool):'Invert the color data IE: Black = White.';self._writecommand(TFT.INVON if aBool else TFT.INVOFF)
	@micropython.native
	def rgb(self,aTF=_C):'True = rgb else bgr';self._rgb=aTF;self._setMADCTL()
	@micropython.native
	def rotation(self,aRot):
		'0 - 3. Starts vertical with top toward pins and rotates 90 deg\n       clockwise each step.';B=aRot;A=self
		if 0<=B<4:C=A.rotate^B;A.rotate=B
		if C&1:A._size=A._size[1],A._size[0];A._offset=A._offset[1],A._offset[0]
		if A.tabcolor==A.GREENTAB128x128:
			if B==0:A._offset=2,1
			elif B==1:A._offset=1,2
			elif B==2:A._offset=2,3
			elif B==3:A._offset=3,2
		A._setMADCTL()
	@micropython.native
	def pixel(self,aPos,aColor):
		'Draw a pixel at the given position';B=aPos;A=self
		if 0<=B[0]<A._size[0]and 0<=B[1]<A._size[1]:A._setwindowpoint(B);A._pushcolor(aColor)
	@micropython.native
	def text(self,aPos,aString,aColor,aFont,aSize=1,nowrap=_A):
		'Draw a text at the given position.  If the string reaches the end of the\n       display it is wrapped to aPos[0] on the next line.  aSize may be an integer\n       which will size the font uniformly on w,h or a or any type that may be\n       indexed with [0] or [1].';B=aFont;A=aSize
		if B==_B:return
		if type(A)==int or type(A)==float:C=A,A
		else:C=A
		D,E=aPos;F=C[0]*B[_D]+1
		for G in aString:
			self.char((D,E),G,aColor,B,C);D+=F
			if D+F>self._size[0]:
				if nowrap:break
				else:E+=B[_E]*C[1]+1;D=aPos[0]
	@micropython.native
	def char(self,aPos,aChar,aColor,aFont,aSizes):
		'Draw a character at the given position using the given font and color.\n       aSizes is a tuple with x, y as integer scales indicating the\n       # of pixels to draw for each pixel in the character.';H=aColor;G=aPos;B=aSizes;A=aFont
		if A==_B:return
		I=A['Start'];M=A['End'];C=ord(aChar)
		if I<=C<=M:
			J=A[_D];K=A[_E];C=(C-I)*J;L=A['Data'][C:C+J];F=G[0]
			if B[0]<=1 and B[1]<=1:
				for D in L:
					E=G[1]
					for N in range(K):
						if D&1:self.pixel((F,E),H)
						E+=1;D>>=1
					F+=1
			else:
				for D in L:
					E=G[1]
					for N in range(K):
						if D&1:self.fillrect((F,E),B,H)
						E+=B[1];D>>=1
					F+=B[0]
	@micropython.native
	def line(self,aStart,aEnd,aColor):
		'Draws a line from aStart to aEnd in the given color.  Vertical or horizontal\n       lines are forwarded to vline and hline.';I=aColor;H=self;D=aEnd;C=aStart
		if C[0]==D[0]:J=D if D[1]<C[1]else C;H.vline(J,abs(D[1]-C[1])+1,I)
		elif C[1]==D[1]:J=D if D[0]<C[0]else C;H.hline(J,abs(D[0]-C[0])+1,I)
		else:
			F,G=C;K,L=D;A=K-F;B=L-G;M=1 if A>0 else-1;N=1 if B>0 else-1;A=abs(A);B=abs(B)
			if A>=B:
				B<<=1;E=B-A;A<<=1
				while F!=K:
					H.pixel((F,G),I)
					if E>=0:G+=N;E-=A
					E+=B;F+=M
			else:
				A<<=1;E=A-B;B<<=1
				while G!=L:
					H.pixel((F,G),I)
					if E>=0:F+=M;E-=B
					E+=A;G+=N
	@micropython.native
	def vline(self,aStart,aLen,aColor):
		'Draw a vertical line from aStart for aLen. aLen may be negative.';D=aStart;A=self;B=clamp(D[0],0,A._size[0]),clamp(D[1],0,A._size[1]);C=B[0],clamp(B[1]+aLen,0,A._size[1])
		if C[1]<B[1]:B,C=C,B
		A._setwindowloc(B,C);A._setColor(aColor);A._draw(aLen)
	@micropython.native
	def hline(self,aStart,aLen,aColor):
		'Draw a horizontal line from aStart for aLen. aLen may be negative.';D=aStart;A=self;B=clamp(D[0],0,A._size[0]),clamp(D[1],0,A._size[1]);C=clamp(B[0]+aLen,0,A._size[0]),B[1]
		if C[0]<B[0]:B,C=C,B
		A._setwindowloc(B,C);A._setColor(aColor);A._draw(aLen)
	@micropython.native
	def rect(self,aStart,aSize,aColor):'Draw a hollow rectangle.  aStart is the smallest coordinate corner\n       and aSize is a tuple indicating width, height.';D=aColor;C=self;B=aSize;A=aStart;C.hline(A,B[0],D);C.hline((A[0],A[1]+B[1]-1),B[0],D);C.vline(A,B[1],D);C.vline((A[0]+B[0]-1,A[1]),B[1],D)
	@micropython.native
	def fillrect(self,aStart,aSize,aColor):
		'Draw a filled rectangle.  aStart is the smallest coordinate corner\n       and aSize is a tuple indicating width, height.';F=aSize;E=aStart;C=self;A=clamp(E[0],0,C._size[0]),clamp(E[1],0,C._size[1]);B=clamp(A[0]+F[0]-1,0,C._size[0]),clamp(A[1]+F[1]-1,0,C._size[1])
		if B[0]<A[0]:D=B[0];B=A[0],B[1];A=D,A[1]
		if B[1]<A[1]:D=B[1];B=B[0],A[1];A=A[0],D
		C._setwindowloc(A,B);G=(B[0]-A[0]+1)*(B[1]-A[1]+1);C._setColor(aColor);C._draw(G)
	@micropython.native
	def circle(self,aPos,aRadius,aColor):
		'Draw a hollow circle with the given radius and color with aPos as center.';F=aColor;E=aRadius;B=aPos;A=self;A.colorData[0]=F>>8;A.colorData[1]=F;O=int(0.7071*E)+1;P=E*E
		for C in range(O):D=int(sqrt(P-C*C));G=B[0]+C;H=B[1]+D;I=B[0]-C;J=B[1]-D;K=B[0]+D;L=B[1]+C;M=B[0]-D;N=B[1]-C;A._setwindowpoint((G,H));A._writedata(A.colorData);A._setwindowpoint((G,J));A._writedata(A.colorData);A._setwindowpoint((I,H));A._writedata(A.colorData);A._setwindowpoint((I,J));A._writedata(A.colorData);A._setwindowpoint((K,L));A._writedata(A.colorData);A._setwindowpoint((K,N));A._writedata(A.colorData);A._setwindowpoint((M,L));A._writedata(A.colorData);A._setwindowpoint((M,N));A._writedata(A.colorData)
	@micropython.native
	def fillcircle(self,aPos,aRadius,aColor):
		'Draw a filled circle with given radius and color with aPos as center';F=aColor;E=aRadius;D=aPos;C=self;I=E*E
		for B in range(E):G=int(sqrt(I-B*B));A=D[1]-G;J=A+G*2;A=clamp(A,0,C._size[1]);H=abs(J-A)+1;C.vline((D[0]+B,A),H,F);C.vline((D[0]-B,A),H,F)
	def fill(A,aColor=BLACK):'Fill screen with the given color.';A.fillrect((0,0),A._size,aColor)
	def image(A,x0,y0,x1,y1,data):A._setwindowloc((x0,y0),(x1,y1));A._writedata(data)
	@micropython.native
	def _setColor(self,aColor):B=aColor;A=self;A.colorData[0]=B>>8;A.colorData[1]=B;A.buf=bytes(A.colorData)*32
	@micropython.native
	def _draw(self,aPixels):
		'Send given color to the device aPixels times.';B=aPixels;A=self;A.dc(1);A.cs(0)
		for E in range(B//32):A.spi.write(A.buf)
		C=int(B)%32
		if C>0:D=bytes(A.colorData)*C;A.spi.write(D)
		A.cs(1)
	@micropython.native
	def _setwindowpoint(self,aPos):'Set a single point for drawing a color to.';A=self;B=A._offset[0]+int(aPos[0]);C=A._offset[1]+int(aPos[1]);A._writecommand(TFT.CASET);A.windowLocData[0]=A._offset[0];A.windowLocData[1]=B;A.windowLocData[2]=A._offset[0];A.windowLocData[3]=B;A._writedata(A.windowLocData);A._writecommand(TFT.RASET);A.windowLocData[0]=A._offset[1];A.windowLocData[1]=C;A.windowLocData[2]=A._offset[1];A.windowLocData[3]=C;A._writedata(A.windowLocData);A._writecommand(TFT.RAMWR)
	@micropython.native
	def _setwindowloc(self,aPos0,aPos1):'Set a rectangular area for drawing a color to.';C=aPos1;B=aPos0;A=self;A._writecommand(TFT.CASET);A.windowLocData[0]=A._offset[0];A.windowLocData[1]=A._offset[0]+int(B[0]);A.windowLocData[2]=A._offset[0];A.windowLocData[3]=A._offset[0]+int(C[0]);A._writedata(A.windowLocData);A._writecommand(TFT.RASET);A.windowLocData[0]=A._offset[1];A.windowLocData[1]=A._offset[1]+int(B[1]);A.windowLocData[2]=A._offset[1];A.windowLocData[3]=A._offset[1]+int(C[1]);A._writedata(A.windowLocData);A._writecommand(TFT.RAMWR)
	@micropython.native
	def _writecommand(self,aCommand):'Write given command to the device.';A=self;A.dc(0);A.cs(0);A.spi.write(bytearray([aCommand]));A.cs(1)
	@micropython.native
	def _writedata(self,aData):'Write given data to the device.  This may be\n       either a single int or a bytearray of values.';A=self;A.dc(1);A.cs(0);A.spi.write(aData);A.cs(1)
	@micropython.native
	def _pushcolor(self,aColor):'Push given color to the device.';B=aColor;A=self;A.colorData[0]=B>>8;A.colorData[1]=B;A._writedata(A.colorData)
	@micropython.native
	def _setMADCTL(self):'Set screen rotation and RGB/BGR format.';A=self;A._writecommand(TFT.MADCTL);B=TFTRGB if A._rgb else TFTBGR;A._writedata(bytearray([TFTRotations[A.rotate]|B]))
	@micropython.native
	def _reset(self):
		'Reset the device.';A=self;A.dc(0)
		if A.useReset:A.reset(1);time.sleep_us(500);A.reset(0);time.sleep_us(500);A.reset(1)
		time.sleep_us(500)
	def init_7735(A,Tabcolor):
		A.tabcolor=Tabcolor
		if A.tabcolor==A.BLUETAB:A._size=128,160;A._offset=2,1;A._rgb=_C;A._reset();A._writecommand(TFT.SWRESET);time.sleep_us(50);A._writecommand(TFT.SLPOUT);time.sleep_us(500);C=bytearray(1);A._writecommand(TFT.COLMOD);C[0]=5;A._writedata(C);time.sleep_us(10);D=bytearray([0,6,3]);A._writecommand(TFT.FRMCTR1);A._writedata(D);time.sleep_us(10);A._writecommand(TFT.MADCTL);C[0]=8;A._writedata(C);B=bytearray(2);A._writecommand(TFT.DISSET5);B[0]=21;B[1]=2;A._writedata(B);A._writecommand(TFT.INVCTR);C[0]=0;A._writedata(C);A._writecommand(TFT.PWCTR1);B[0]=2;B[1]=112;A._writedata(B);time.sleep_us(10);A._writecommand(TFT.PWCTR2);C[0]=5;A._writedata(C);A._writecommand(TFT.PWCTR3);B[0]=1;B[1]=2;A._writedata(B);A._writecommand(TFT.VMCTR1);B[0]=60;B[1]=56;A._writedata(B);time.sleep_us(10);A._writecommand(TFT.PWCTR6);B[0]=17;B[1]=21;A._writedata(B);E=bytearray([2,28,7,18,55,50,41,45,41,37,43,57,0,1,3,16]);A._writecommand(TFT.GMCTRP1);A._writedata(E);F=bytearray([3,29,7,6,46,44,41,45,46,46,55,63,0,0,2,16]);A._writecommand(TFT.GMCTRN1);A._writedata(F);time.sleep_us(10);A._writecommand(TFT.CASET);A.windowLocData[0]=0;A.windowLocData[1]=A._offset[0];A.windowLocData[2]=0;A.windowLocData[3]=A._size[0]+A._offset[0];A._writedata(A.windowLocData);A._writecommand(TFT.RASET);A.windowLocData[1]=A._offset[1];A.windowLocData[3]=A._size[1]+A._offset[1];A._writedata(A.windowLocData);A._writecommand(TFT.NORON);time.sleep_us(10);A._writecommand(TFT.RAMWR);time.sleep_us(500);A._writecommand(TFT.DISPON);A.cs(1);time.sleep_us(500)
		else:
			A._reset();A._writecommand(TFT.SWRESET);time.sleep_us(150);A._writecommand(TFT.SLPOUT);time.sleep_us(255);D=bytearray([1,44,45]);A._writecommand(TFT.FRMCTR1);A._writedata(D);A._writecommand(TFT.FRMCTR2);A._writedata(D);G=bytearray([1,44,45,1,44,45]);A._writecommand(TFT.FRMCTR3);A._writedata(G);time.sleep_us(10);A._writecommand(TFT.INVCTR);A._writedata(bytearray([7]));A._writecommand(TFT.PWCTR1);D[0]=162;D[1]=2;D[2]=132;A._writedata(D);A._writecommand(TFT.PWCTR2);A._writedata(bytearray([197]));B=bytearray(2);A._writecommand(TFT.PWCTR3);B[0]=10;B[1]=0;A._writedata(B);A._writecommand(TFT.PWCTR4);B[0]=138;B[1]=42;A._writedata(B);A._writecommand(TFT.PWCTR5);B[0]=138;B[1]=238;A._writedata(B);A._writecommand(TFT.VMCTR1);A._writedata(bytearray([14]));A._writecommand(TFT.INVOFF)
			if A.tabcolor==A.GREENTAB:A._offset=2,1
			if A.tabcolor==A.REDTAB:A._offset=0,0
			if A.tabcolor==A.BLACKTAB:A._offset=0,0;A._rgb=_A
			elif A.tabcolor==A.GREENTAB2:A._offset=2,1;A._rgb=_A
			elif A.tabcolor==A.GREENTAB3:A._offset=2,3
			elif A.tabcolor==A.GREENTAB128x128:A._size=128,128;A._offset=2,1;A._rgb=_A
			elif A.tabcolor==A.GREENTAB80x160:A._size=80,160;A._offset=26,1;A._rgb=_A;A._writecommand(TFT.INVON)
			elif A.tabcolor==A.REDTAB80x160:A._size=80,160;A._offset=24,0
			if A.tabcolor==A.GREENTAB80x160 or A.tabcolor==A.REDTAB80x160:A.rotation(1)
			else:A.rotation(2)
			A._setMADCTL();A._writecommand(TFT.COLMOD);A._writedata(bytearray([5]));A._writecommand(TFT.CASET);A.windowLocData[0]=0;A.windowLocData[1]=A._offset[0];A.windowLocData[2]=0;A.windowLocData[3]=A._size[0]+A._offset[0];A._writedata(A.windowLocData);A._writecommand(TFT.RASET);A.windowLocData[1]=A._offset[1];A.windowLocData[3]=A._size[1]+A._offset[1];A._writedata(A.windowLocData);E=bytearray([2,28,7,18,55,50,41,45,41,37,43,57,0,1,3,16]);A._writecommand(TFT.GMCTRP1);A._writedata(E);F=bytearray([3,29,7,6,46,44,41,45,46,46,55,63,0,0,2,16]);A._writecommand(TFT.GMCTRN1);A._writedata(F);A._writecommand(TFT.NORON);time.sleep_us(10);A._writecommand(TFT.DISPON);time.sleep_us(100);A.cs(1)