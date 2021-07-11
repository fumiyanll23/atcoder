def main():
    # input
    N, M, T = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(M)]

    # compute
    now = 0
    battery = N
    for A, B in ABs:
        battery -= A - now
        if battery <= 0:
            print('No')
            exit()
        now = A
        battery = min(battery+B-A, N)
        now = B
    battery -= T - now
    if battery <= 0:
        print('No')
        exit()

    # output
    print('Yes')


if __name__ == '__main__':
    main()
