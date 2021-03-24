Sensor_limits = { 'soc' : 0.05 , 'curr' : 0.1 }

def  Setting_up_thresholds(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def validate_none(values):
  if values is not None:
    return validate_soc_reading(values, sensor_param_name)
  return False

def validate_soc_reading(values, sensor_param_name):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(not Setting_up_thresholds(values[i], values[i + 1], sensor_limits[sensor_param_name])):
    return False
  return True
     


