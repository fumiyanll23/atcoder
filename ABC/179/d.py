N, K = map(int, input().split())
L = [0 for i in range(K)]
R = [0 for i in range(K)]
for i in range(K):
  L[i], R[i] = map(int, input().split())
mod = 998244353

print(N, K)
print(L)
print(R)