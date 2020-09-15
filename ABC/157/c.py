N, M = map(int, input().split())
s = [0 for i in range(M)]
c = [0 for i in range(M)]
for i in range(M):
  s[i], c[i] = map(int, input().split())

ans = [0, 0, 0]
for i in range(M):
  ans[s[i]-1] = c[i]

"""
Add codes here
"""
print(ans[0]*100 + ans[1]*10 + ans[2])