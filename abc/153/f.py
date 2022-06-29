import numpy as np

N, D, A = map(int, input().split())
monster = [[0, 0] for i in range(N)]
for i in range(N):
  monster = list(map(int, input().split()))

monster = np.sort(magic, axis = 0)
monster = np.sort(magic, axis = 1)
monster = tolist(magic) # Convert to list type