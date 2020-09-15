N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

flag = True
# ダブリのカウント
cnt = 0
for i in range(N):
  for j in range(N):
    if A[i] == B[j]:
      cnt += 1
if cnt >= (N+1)//2:
  flag = False