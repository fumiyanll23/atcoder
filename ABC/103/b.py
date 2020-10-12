S = str(input())
T = str(input())

N = len(S)
test = S * 2
flag = False
for i in range(2*N):
  if test[i:N+i] == T:
    flag = True
    break

if flag:
  print('Yes')
else:
  print('No')
