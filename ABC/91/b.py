N = int(input())
s = [str(input()) for _ in range(N)]
M = int(input())
t = [str(input()) for _ in range(M)]

u = s.extend(t)
blue = [1 for _ in range(N)]
red = [1 for _ in range(M)]
for i in range(N+M):
  for j in range(i+1, N+M):
    if s[i] == s[j]:
      if i < N:
        blue[i] += 1
      else:
        red[i-N] += 1
print(blue)
print(red)
