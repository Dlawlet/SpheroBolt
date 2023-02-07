import random

curDirection = 45

left_bound = curDirection - 105
right_bound = curDirection + 105

if left_bound < 0:
  left_bound += 360
  right_bound += 360
  print(left_bound%360, right_bound%360)
  new_direction = random.randint(min(left_bound%360, right_bound%360),max(left_bound%360, right_bound%360))
else:
  print("yo",left_bound%360, right_bound%360)
  new_direction = random.randint(min(left_bound%360, right_bound%360),max(left_bound%360, right_bound%360))

print("New direction:", new_direction)