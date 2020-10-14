N = int(input())
L = list(map(int, input().split()))

if(N <= 2):
  print(0)
else:
  L.sort()
  cnt = 0
  for i in range(N):
    for j in range(i, N):
      for k in range(j, N):
        if L[i]!=L[j] and L[j]!=L[k] and L[k]!=L[i]:
          if L[i]<=L[j]+L[k] and L[j]<=L[k]+L[i] and L[k]<=L[i]+L[j]:
            cnt += 1
print(cnt)

### Give up...
