N = int(input())
S = [input().split() for i in range(N)]

ac, wa, tle, re = 0, 0, 0, 0
for i in range(N):
  if(S[i] == 'AC'):
    ac += 1
  elif(S[i] == 'WA'):
    wa += 1
  elif(S[i] == 'TLE'):
    tle += 1
  else:
    re += 1

print("AC x", ac)
print("WA x", wa)
print("TLE x", tle)
print("RE x", re)