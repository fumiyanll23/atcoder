def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    diffs = [0] * (N-1)
    r, s = 0, sum(As)
    for i in range(N-1):
        r += As[i]
        s -= As[i]
        diffs[i] = abs(s-r)

    # output
    print(min(diffs))


if __name__ == '__main__':
    main()
