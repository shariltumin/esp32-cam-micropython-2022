
from AXP2101 import *
from machine import Pin, I2C

def cam_power_on():
   SDA = 7
   SCL = 6
   IRQ = 2
   I2CBUS = I2C(1, scl=Pin(SCL), sda=Pin(SDA))
   # I2CBUS.scan()
   # [52, 60]
   PMU = AXP2101(I2CBUS, addr=AXP2101_SLAVE_ADDRESS)
   id = PMU.getChipID()
   if id != XPOWERS_AXP2101_CHIP_ID:
      print("PMU is not online...")
   else:
      print('getID:%s' % hex(PMU.getChipID()))

      # Set the working voltage of the camera, 
      # --* please do not modify the parameters--*
      PMU.setALDO1Voltage(1800)  # CAM DVDD  1500~1800
      PMU.enableALDO1()
      PMU.setALDO2Voltage(2800)  # CAM DVDD 2500~2800
      PMU.enableALDO2()
      PMU.setALDO4Voltage(3000)  # CAM AVDD 2800~3000
      PMU.enableALDO4()

      # TS Pin detection must be disable, otherwise it cannot be charged
      PMU.disableTSPinMeasure()

