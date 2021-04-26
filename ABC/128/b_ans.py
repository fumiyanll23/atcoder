def main():
    # input
    N = int(input())
    SPs = [input().split() for _ in range(N)]
    SPs = list(map(lambda x: (x[1][0], int(x[1][1]), x[0]), enumerate(SPs))) # enumerate()を利用しているのでx[0]にはインデックスが格納されている

    # compute
    SPs.sort(key=lambda x: x[1], reverse=True)
    SPs.sort(key=lambda x: x[0])

    # output
    for _, _, i in SPs:
        print(i+1)


if __name__ == '__main__':
    main()
