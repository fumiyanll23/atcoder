# input
hws = [*map(int, input().split())]

# compute
new_hws = [hw - 3 for hw in hws]
hs = new_hws[:3]
ws = new_hws[3:]

# output
if sum(hs) == sum(ws):
    print(new_hws)
else:
    print(0)
