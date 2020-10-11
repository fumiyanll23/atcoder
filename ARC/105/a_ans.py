d = list(map(int, input().split()))

d.sort()
if d[0]+d[3]==d[1]+d[2] or d[3]==d[0]+d[1]+d[2]:
  print('Yes')
else:
  print('No')
