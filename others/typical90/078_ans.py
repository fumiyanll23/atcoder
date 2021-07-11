def main():
    # input
    N, M = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(M)]

    # compute
    cnts = [0] * N
    for A, B in ABs:
        cnts[max(A,B)-1] += 1

    # output
    print(cnts.count(1))


if __name__ == '__main__':
    main()
