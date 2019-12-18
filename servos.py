import Adafruit_PCA9685
import time

# Initialise the PCA9685 using the default address (0x40).
PCA9685_pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Set frequency to 100hz, good for l298n h-bridge.
PCA9685_pwm.set_pwm_freq(60)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 520  # Max pulse length out of 4096

def set_grabber(value):
  PCA9685_pwm.set_pwm(0, 0, int(value))

def set_elbow(value):
  PCA9685_pwm.set_pwm(1, 0, int(value))
  
def set_shoulder(value):
  PCA9685_pwm.set_pwm(2, 0, int(value))
  
def set_base(value):
  PCA9685_pwm.set_pwm(3, 0, int(value))