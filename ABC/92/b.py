N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

choco = []
for i in range(N):
  choco.append((D-1) // A[i])
print(N + X + sum(choco))
