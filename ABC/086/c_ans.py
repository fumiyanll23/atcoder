def main():
    # input
    N = int(input())
    txys = [list(map(int, input().split())) for _ in range(N)]

    # compute
    flag = True
    t1, x1, y1 = 0, 0, 0
    for t2, x2, y2 in txys:
        dt, dxy = t2-t1, abs(x2-x1)+abs(y2-y1)
        if not(dt>=dxy and (dxy-dt)%2==0):
            flag = False
        t1, x1, y1 = t2, x2, y2,

    # output
    if flag:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
