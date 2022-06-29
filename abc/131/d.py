def main():
    # input
    N = int(input())
    ABs = [[*map(int, input().split())] for _ in range(N)]

    # compute
    ABs.sort(key=lambda x: x[1])
    now = 0
    for A, B in ABs:
        if now+A <= B:
            now += A
        else:
            print('No')
            exit()

    # output
    print('Yes')


if __name__ == '__main__':
    main()
