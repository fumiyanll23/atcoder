# Input 
H, W = map(int, input().split())
a = []
for _ in range(H):
  a.append(list(str(input())))

# Check every row -> column
for i in range(H):
  white = 0
  for j in range(W):
    if a[i][j] == '.':
      white += 1
  if white == W:
    for j in range(W):
      a[i][j] = ''
# Check every column -> row
for j in range(W):
  white = 0
  for i in range(H):
    if a[i][j] == '.':
      white += 1
  if white == H:
    for i in range(H):
      a[i][j] = ''

# Output
ans = ['' for _ in range(H)]
for i in range(H):
  for j in range(W):
    ans[i] += a[i][j]
ansans = '\n'.join(ans)
print(ansans)

### How remove '.' at cross points?