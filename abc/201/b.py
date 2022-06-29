def main():
    # input
    N = int(input())
    STs = [list(input().split()) for _ in range(N)]

    # compute
    for i,st in enumerate(STs):
        STs[i][1] = int(st[1])
    STs.sort(key=lambda x: x[1])

    # output
    print(STs[-2][0])


if __name__ == '__main__':
    main()
