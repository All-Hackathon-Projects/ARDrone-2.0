import sensor_data_pb2

def take_picture(input):
	has_command = input['is_running']
	meta_id = 'nothing'
	data = ''

	encodedsd = input['sensors']
	decodedsd = sensor_data_pb2.SensorData().FromString(encodedsd)

	# Get Image Constraints
	#Image.frombytes('RGB', (decodedsd.images[0].width, decodedsd.images[0].height), decodedsd.images[0].image_data).show()
	print("Picture Scheduled")
	data = {
        'width': decodedsd.images[0].width 
      	'height': decodedsd.images[0].height
      	'bytes': decodedsd.images[0].image_data
    }

	return {
        'has_command': has_command,  
        'meta_id': 'take_pic',
        'data': data,
    }