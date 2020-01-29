import Adafruit_PCA9685
from time import sleep

class Servo():

  def __init__(self):
    self.PCA9685_pwm = Adafruit_PCA9685.PCA9685()
    self.PCA9685_pwm.set_pwm_freq(60)
    self.grabber = 400
    self.elbow = 270
    self.shoulder = 460
    self.base = 310

  def set_grabber(self, value):
    self.PCA9685_pwm.set_pwm(0, 0, int(value))
    self.grabber = int(value)

  def set_elbow(self, value):
    self.PCA9685_pwm.set_pwm(1, 0, int(value))
    self.elbow = int(value)

  def set_shoulder(self, value):
    self.PCA9685_pwm.set_pwm(2, 0, int(value))
    self.shoulder = int(value)

  def set_base(self, value):
    self.PCA9685_pwm.set_pwm(3, 0, int(value))
    self.base = int(value)

  def set_elbowlerp(self, value):
    old = self.elbow
    inc = 1
    if old > int(value):
      inc = -1
    print("start")
    for x in range(old, int(value), inc):
      self.set_elbow(x)
      print("x: " + str(x))
      sleep(0.002)

  def set_shoulderlerp(self, value):
    old = self.shoulder
    inc = 1
    if old > int(value):
      inc = -1
    print("start")
    for x in range(old, int(value), inc):
      self.set_shoulder(x)
      print("x: " + str(x))
      sleep(0.002)

  def set_baselerp(self, value):
    old = self.base
    inc = 1
    if old > int(value):
      inc = -1
    print("start")
    for x in range(old, int(value), inc):
      self.set_base(x)
      print("x: " + str(x))
      sleep(0.002)

  def move_block(self, values):
    target_elbow = values[0]
    target_shoulder = values[1] - 100
    target_base = values[2]

    inc_elbow = 1
    inc_shoulder = 1
    inc_base = 1

    if self.elbow > target_elbow:
      inc_elbow = -1
    if self.shoulder > target_shoulder:
      inc_shoulder = -1
    if self.base > target_base:
      inc_base = -1

    finished_elbow = False
    finished_shoulder = False
    finished_base = False

    while not finished_elbow or not finished_shoulder or not finished_base:
      if self.elbow == target_elbow:
        finished_elbow = True
      if self.shoulder == target_shoulder:
        finished_shoulder = True
      if self.base == target_base:
        finished_base = True

      if not finished_elbow:
        self.set_elbow(self.elbow + inc_elbow)
      if not finished_shoulder:
        self.set_shoulder(self.shoulder + inc_shoulder)
      if not finished_base:
        self.set_base(self.base + inc_base)
      sleep(0.002)
      pass
    self.lower_shoulder()
  pass

  def set_smooth(self, values):
    target_elbow = values[0]
    target_shoulder = values[1]
    target_base = values[2]

    inc_elbow = 1
    inc_shoulder = 1
    inc_base = 1

    if self.elbow > target_elbow:
      inc_elbow = -1
    if self.shoulder > target_shoulder:
      inc_shoulder = -1
    if self.base > target_base:
      inc_base = -1

    finished_elbow = False
    finished_shoulder = False
    finished_base = False

    while not finished_elbow or not finished_shoulder or not finished_base:
      if self.elbow == target_elbow:
        finished_elbow = True
      if self.shoulder == target_shoulder:
        finished_shoulder = True
      if self.base == target_base:
        finished_base = True

      if not finished_elbow:
        self.set_elbow(self.elbow + inc_elbow)
      if not finished_shoulder:
        self.set_shoulder(self.shoulder + inc_shoulder)
      if not finished_base:
        self.set_base(self.base + inc_base)
      sleep(0.002)
      pass
  pass

  def set_grabber_smooth(self, value):
    target_grabber = value

    inc_grabber = 1

    if self.grabber > target_grabber:
      inc_grabber = -1

    finished_grabber = False

    while not finished_grabber:
      if self.grabber == target_grabber:
        finished_grabber = True

      if not finished_grabber:
        self.set_grabber(self.grabber + inc_grabber)
      sleep(0.005)
  pass

  def lift_shoulder(self):
    target_shoulder = self.shoulder - 100

    inc_shoulder = 1

    if self.shoulder > target_shoulder:
      inc_shoulder = -1

    finished_shoulder = False

    while not finished_shoulder:
      if self.shoulder == target_shoulder:
        finished_shoulder = True

      if not finished_shoulder:
        self.set_shoulder(self.shoulder + inc_shoulder)
      sleep(0.005)
  pass

  def lower_shoulder(self):
    target_shoulder = self.shoulder + 100

    inc_shoulder = 1

    if self.shoulder > target_shoulder:
      inc_shoulder = -1

    finished_shoulder = False

    while not finished_shoulder:
      if self.shoulder == target_shoulder:
        finished_shoulder = True

      if not finished_shoulder:
        self.set_shoulder(self.shoulder + inc_shoulder)
      sleep(0.005)
  pass
