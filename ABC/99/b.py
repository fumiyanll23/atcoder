a, b = map(int, input().split())

h, i = 0, 1
while h <= a:
  h += i
  i += 1
print(h - a)
