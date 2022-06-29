def main():
    # input
    N, M = map(int, input().split())
    As = [*map(int, input().split())]
    Bs = [*map(int, input().split())]

    # compute
    As.sort()
    Bs.sort()
    ans = abs(As[0] - Bs[0])
    i, j = 0, 0
    while i != N-1 and j != M-1:
        if As[i] <= Bs[j]:
            i += 1
        else:
            j += 1
        ans = min(ans, abs(As[i]-Bs[j]))

    # output
    print(ans)


if __name__ == '__main__':
    main()
