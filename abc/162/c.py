import math
K = int(input()) + 1

ans = 0
for i in range(K):
  for j in range(K):
    for k in range(K):
      ans += math.gcd(math.gcd(i, j), k)
print(ans)

# Not matched.