def main():
    # input
    N, K = map(int, input().split())
    As = list(map(int, input().split()))

    # compute
    As.sort()
    total = 0
    cnts = [0] * N
    for i in As:
        cnts[i] += 1
    min_like = K
    for i in cnts:
        min_like = min(min_like, i)
        total += min_like

    # output
    print(total)


if __name__ == '__main__':
    main()
