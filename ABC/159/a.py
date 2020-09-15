# Define factoriral(n); n!
def myfact(a):
  if a <= 1:
    return 1
  else:
    return myfact(a) * myfact(a-1)

# Define combination(n, r); nCr
def mycmb(b, c):
  if b <= c or c < 0:
    return 1
  else:
    return myfact(b) // myfact(c) // myfact(b-c)

N, M = map(int, input().split())

### For test
print(myfact(N))
print(myfact(M))
print(mycmb(N, 2))
print(mycmb(M, 2))
###
print(mycmb(N, 2) + mycmb(M, 2))

# Error??