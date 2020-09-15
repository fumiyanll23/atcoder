K = int(input())
S = input()

if(len(S) <= K):
  print(S)
else:
  S[K] = '...'
  print(S[0, K])

# TypeError: 'str' object does not support item assignment