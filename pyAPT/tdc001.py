import controller

class TDC001(controller.ControllerSerial):
  """
  A controller for a TDC001/Z825B stage connected via a serial port.
  """
  def __init__(self, *args, **kwargs):
    super(TDC001, self).__init__(*args, **kwargs)

    #http://www.thorlabs.com/thorproduct.cfm?partnumber=TDC001
    # Note that these values are pulled from the APT User software,
    # as they agree with the real limits of the stage better than
    # what the website or the user manual states
    self.max_velocity = 2.0
    self.max_acceleration = 2.0

    # steps per revolution: 512
    # gearbox ratio: 67
    # pitch: 1.0 mm
    # thus to advance 1 mm you need to turn 48*256*1 times
    enccnt = 67*512*1
    T = 2048/6e6

    # these equations are taken from the APT protocol manual
    self.position_scale = enccnt
    self.velocity_scale = enccnt * T * 65536
    self.acceleration_scale = enccnt * T * T * 65536

    self.linear_range = (0,50)

