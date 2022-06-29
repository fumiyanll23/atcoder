A, B = map(int, input().split())
S = str(input())

flag = True
if not S[:A].isdecimal():
  flag = False
elif S[A] != '-':
  flag = False
elif not S[-B:].isdecimal():
  flag = False
if flag:
  print('Yes')
else:
  print('No')
