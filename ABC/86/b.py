import math

a, b = map(str, input().split())

num = int(a + b)
snum = math.sqrt(num)
if snum.is_integer():
  print('Yes')
else:
  print('No')
