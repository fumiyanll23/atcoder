# input
hws = [*map(int, input().split())]

# compute
hs = hws[:3]
ws = hws[3:]
ans = 0
for a in range(1, 29):
    for b in range(1, 29):
        for d in range(1, 29):
            for e in range(1, 29):
                c = hs[0] - a - b
                f = hs[1] - d - e
                g = ws[0] - a - d
                h = ws[1] - b - e
                i = ws[2] - c - f
                if min((c, f, g, h, i)) > 0 and g + h + i == hs[2]:
                    ans += 1

# output
print(ans)
