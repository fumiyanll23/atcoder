### From "https://kenkoro.hatenablog.com/entry/2019/07/17/220000"

N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
for i in range(N):
  if V[i] > C[i]:
    ans += V[i] - C[i]
print(ans)