N, L = map(int, input().split())

taste = [L+i for i in range(N)]
taste_abs = []
for i in range(N):
  taste_abs.append(abs(taste[i]))
eat = min(taste_abs)
print(eat)
#print(sum(taste) - taste[eat])