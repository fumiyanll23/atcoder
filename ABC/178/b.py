a, b, c, d = map(int, input().split())

ans = [0 for i in range(4)]
ans[0] = a * c
ans[1] = a * d
ans[2] = b * c
ans[3] = b * d
print(max(ans))