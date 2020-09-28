import numpy as np

N, M = map(int, input().split())
drink = []
for i in range(N):
  drink.append(list(map(int, input().split())))

cost, cnt = 0, 0
drink = np.sort(drink, axis=0).tolist()
i = 0
while cnt < M:
  cnt += drink[i][1]
  i += 1

### Too confused...