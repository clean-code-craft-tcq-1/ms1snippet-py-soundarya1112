
def  Setting_up_thresholds(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def validate_soc_reading(values):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
   equality = "is False" if(not Setting_up_thresholds(values[i], values[i + 1], 0.05)) else "is True" if(not Setting_up_thresholds(values[i], values[i + 1], 0.1)) else "is None" if values is None 
   return equality

