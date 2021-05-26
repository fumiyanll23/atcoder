from math import ceil

def main():
    # input
    N, M = map(int, input().split())
    As = [*map(int, input().split())]

    # compute
    if N == M:
        print(0)
    elif M == 0:
        print(1)
    else:
        As.sort()
        if As[0] != 1:
            As.insert(0, 0)
        if As[-1] != N:
            As.append(N+1)
        print(As)
        cnts, tmp = [], 0
        for i in range(M-1):
            if As[i]-tmp-1 != 0:
                cnts.append(As[i]-tmp-1)
            tmp = As[i]
        if As[-1]-tmp-1 != 0:
            cnts.append(As[-1]-tmp-1)
        print(cnts)

    # output


if __name__ == '__main__':
    main()
