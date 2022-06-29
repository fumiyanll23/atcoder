import numpy as np

H, N = map(int, input().split())
magic = [[0, 0] for i in range(N)]
for i in range(N):
  magic[i] = list(map(int, input().split()))

magic = np.sort(magic, axis = 0)
magic = np.sort(magic, axis = 1)
magic = tolist(magic) # Convert to list type