N, D = map(int, input().split())
X, Y = list(map(int, input().split()))
cnt = 0

for i in range(N):
  if(D**2 >= (X[i]**2 + Y[i]**2)):
    cnt += 1

print(cnt)