S = str(input())

if S[-1] == 's':
  ans = S + 'es'
else:
  ans = S + 's'
print(ans)