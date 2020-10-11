deli = list(map(int, input().split()))

flag = False
deli.sort(reverse=True)
for i in range(3):
  for j in range(i+1, 4):
    if deli[i] == sum(deli)-deli[i]:
      flag = True
    elif deli[i]+deli[j] == sum(deli)-deli[i]-deli[j]:
      flag = True
if flag:
  print('Yes')
else:
  print('No')
