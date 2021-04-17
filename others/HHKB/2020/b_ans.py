H, W = map(int, input().split())
S = [str(input()) for _ in range(H)]

ans = 0
for i in range(H):
  for j in range(W):
    if i+1<H and S[i][j]==S[i+1][j] and S[i][j]=='.':
      ans += 1
    if j+1<W and S[i][j]==S[i][j+1] and S[i][j]=='.':
      ans += 1
print(ans)