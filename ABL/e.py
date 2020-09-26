N, Q = map(int, input().split())
L = [0 for i in range(Q)]
R = [0 for i in range(Q)]
D = [0 for i in range(Q)]
for i in range(Q):
  L[i], R[i], D[i] = map(int, input().split())
  D[i] = str(D[i])
mod = 998244353

S = ['1' for i in range(N)]
