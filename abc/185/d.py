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
        masss = ['W'] * N
        for A in As:
            masss[A-1] = 'B'
        cnts = [0] * N
        if masss[0] == 'W':
            cnts[0] = 1
        for i in range(1,N):
            if masss[i] == 'W':
                cnts[i] = cnts[i-1] + 1
        maxs = []
        for A in As:
            maxs.append(cnts[A-1])
        if cnts[-1] != 0:
            maxs.append(cnts[-1])
        k = min(maxs)
        ans = 0
        for maxsi in maxs:
            ans += ceil(maxsi/k)
        print(ans)

    # output


if __name__ == '__main__':
    main()
