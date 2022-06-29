A, B, X = map(int, input().split())

flag = False
if A <= X <= A+B:
  flag = True
if flag:
  print('YES')
else:
  print('NO')
