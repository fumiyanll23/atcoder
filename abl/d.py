N, K = map(int, input().split())
A = [0 for i in range(N)]
for i in range(N):
  A[i] = int(input())

B = []
for i in range(N-2):
  if abs(A[i]-A[i+1])<=K and abs(A[i+1]-A[i+2])<=K:
    B.append(A[i])
print(len(B))

### 隣り合う項以外も探索する