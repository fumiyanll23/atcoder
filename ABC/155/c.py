N = int(input())
S = ['a' for i in range(N)]
for i in range(N):
  S[i] = str(input())

ans = [0 for i in range(N)]
for i in range(N):
  for j in range(N):
    if S[i] == S[j]:
      ans[] += 1 # What are their indexes?
    else:
      ans[] = S[j] # What are ...?