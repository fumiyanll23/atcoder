def func(x1, y1, x2, y2, x=0):
    return (y2-y1)/(x2-x1)*(x-x1) + y1

def main():
    # input
    N, D, H = map(int, input().split())
    dhs = [list(map(int, input().split())) for _ in range(N)]

    # compute
    hights = [0]
    for dh in dhs:
        hights.append(func(dh[0], dh[1], D, H))

    # output
    print(max(hights))


if __name__ == '__main__':
    main()
