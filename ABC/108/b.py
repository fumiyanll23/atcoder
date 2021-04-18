from math import sqrt

def main():
    # input
    x1, y1, x2, y2 = map(int, input().split())

    # compute
    dots = []
    edge = sqrt((x1-x2)**2+(y1-y2)**2)
    for x3 in range(-100, min(x1,x2)):
        for y3 in range(-100, 101):
            for x4 in range(-100, 101):
                for y4 in range(-100, 101):
                    if (x3-x4)*(x1-x2) == (y3-y4)*(y1-y2):
                        if sqrt((x3-x4)**2+(y3-y4)**2) == edge:
                            if sqrt((x1-x3)**2+(y1-x4)**2) == edge:
                                if sqrt((x2-y3)**2+(y2-y4)**2) == edge:
                                    dots.append([x3, x4, y3, y4])

    # output
    print(dots)


if __name__ == '__main__':
    main()
