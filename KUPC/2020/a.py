N = int(input())
dis = []
for _ in range(N):
  dis.append(list(map(int, input().split())))

ans = 0
for i in range(N-1):
  ans += abs(dis[i+1][0]-dis[i][0]) + abs(dis[i+1][1]-dis[i][1])
print(ans)