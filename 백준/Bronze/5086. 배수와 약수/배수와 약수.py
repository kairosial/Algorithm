while True:
  a, b = map(int, input().split())
  try:
    if a == 0 and b == 0:
      break
    elif a == 0 or b == 0:
      pass
    elif b % a == 0:
      print('factor')
    elif a % b == 0:
      print('multiple')
    else:
      print('neither')
  except ZeroDivisionError:
    pass