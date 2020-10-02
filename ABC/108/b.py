x1, y1, x2, y2 = map(int, input().split())

width = abs(x1 - x2)
height = abs(y1 - y2)
if x1<=x2 and y1<=y2:

elif x1<=x2 and y1>y2:

elif x1>x2 and y1<=y2:

else: