H, W = map(int, input().split())
S = [str(input()) for _ in range(H)]

row = 0
for i in range(H):
  for j in range(W-1):
    if S[i][j]==S[i][j+1] and S[i][j]=='.':
      row += 1
column = 0
for i in range(W):
  for j in range(H-1):
    if S[j][i]==S[j+1][i] and S[j][i]=='.':
      column += 1
print(row + column)