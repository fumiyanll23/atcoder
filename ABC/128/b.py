import numpy as np

N = int(input())
rest = []
for i in range(N):
  rest.append(list(map(str, input().split())))
  rest[i][1] = int(rest[i][1])
print(N)
print(rest)