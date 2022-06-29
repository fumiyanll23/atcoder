N = int(input())

SN = sum(list(map(int, str(N))))
if N%SN == 0:
  print('Yes')
else:
  print('No')
