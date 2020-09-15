K = int(input())
A, B = map(int, input().split())

if(B-A+1 >= K or K == 1):
  print("OK")
else:
  print("NG")

# WA * 2...