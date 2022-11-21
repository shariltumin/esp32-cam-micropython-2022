MicroPython v1.19.1-705-gac5934c96 2022-11-21

Compiled with *esp-idf-442*

What NOT include:
  1. help
  2. SSL
  3. I2S
  4. BLE
  5. webrepl
  6. machine.adc
  7. machine.dac

Camera module:
  1. OV2640 AI Thinker board only
  2. I2C peripheral to use for SCCB: i2c-port0
  3. Camera task pinned to core: CAMERA_CORE1
  4. camera_config.xclk_freq_hz=18000000
  5. now include hmirror as camera.mirror()

