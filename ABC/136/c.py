N = int(input())
H = list(map(int, input().split()))

flag = True
for i in range(N-1):
  if abs(H[i]-H[i+1]) == 1:
    flag = False
if flag:
  print("Yes")
else:
  print("No")