from parse_sensor_data import drone

def disconnect(command_data):
	drone.halt()

def calibrate(command_data):
	drone.trim()
def takeoff(command_data):
	drone.takeoff()
def hover(command_data):
	drone.hover()
def land(command_data):
	drone.land()

def speed(command_data):
	drone.set_speed(0.5)

def up(command_data):
  drone.move_up()
def down(command_data):
  drone.move_down()
def left(command_data):
  drone.move_left()
def right(command_data):
  drone.move_right()
def forward(command_data):
  drone.move_forward()
def backward(command_data):
  drone.move_backward()

def set_cam(command_data):
	drone.set_cam(0)
def take_pic(command_data):
  pass

metaCommands = {
  'halt': disconnect,

  'calibrate': calibrate,
  'takeoff': takeoff,
  'hover': hover,
  'land': land,

  'speed': speed,

  'left': left,
  'right': right,
  'up': up,
  'down': down,
  'forward': forward,
  'backward': backward,

  'change_camera': set_cam,
  'take_pic': take_pic,
}