L, R = map(int, input().split())

ans = [0 for i in range(R)]
for i in range(L,R):
  for j in range(i, R):
    ans[i] = (i*j) % 2019
print(min(ans))

# Always output '0'...