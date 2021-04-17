from math import sqrt

N = int(input())
n = int(sqrt(N))
stick = [2*(i+1)-1 for i in range(N)]

if N%2 == 0:
  print(N // 2)
  for i in range(N//2):
    print(2, stick[i], stick[-(i+1)])
elif n**2 == N:
  idx = [(i%n-i//n)%n for i in range(n)]
  print(n)
  for i in range(n):
else:
  print('impossible')
