def facial_recognition(sensors_and_state):
	return {
	  'has_command': True,
	  'meta_id': 'calibrate',
	  'data': 'high_priority data',
    }

def object_recognition(sensors_and_state):
	return {
      'has_command': True,  
      'meta_id': 'calibrate',
      'data': 'low_priority data id',
    }

def take_picture(sensors_and_state):
	return {
      'has_command': True,  
      'meta_id': 'calibrate',
      'data': 'low_priority data id',
    }

def vertical_flight(sensors_and_state):
	return {
	    'has_command': True,
	    'meta_id': 'calibrate',
	    'data': 'high_priority data',
    }

modules = [
	facial_recognition,
	object_recognition,
	take_picture,
	vertical_flight,
]