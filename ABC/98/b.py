N = int(input())
S = str(input())

cnt = [0 for _ in range(N)]
for i in range(N):
  X = S[:i]
  Y = S[i:]
  for j in range(26):
    alph = chr(97 + j)
    if (alph in X) and (alph in Y):
      cnt[i] += 1
print(max(cnt))
