X = int(input())

ans = 1
for i in range(1, 32):
  for j in range(2, 100):
    if ans <= i**j <= X:
      ans = i ** j
print(ans)
