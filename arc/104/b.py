n, S = map(str, input().split())
N = int(n)

cnt = 0
for i in range(N-1):
  for j in range(2, N+1-i):
    test = S[i:i+j]
    if test.count('A')==test.count('T') and test.count('C')==test.count('G'):
      cnt += 1

print(cnt)