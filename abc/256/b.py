# input
N = int(input())
As = [*map(int, input().split())]

# compute
P = 0
tiles = [0] * 4
for A in As:
    tiles[0] = 1
    for i in range(3, -1, -1):
        if i + A >= 4:
            P += tiles[i]
        else:
            tiles[i+A] += tiles[i]
        tiles[i] = 0

# output
print(P)
