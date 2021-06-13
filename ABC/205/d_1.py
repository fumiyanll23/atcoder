def main():
    # input
    N, Q = map(int, input().split())
    As = [*map(int, input().split())]
    Ks = [int(input()) for _ in range(Q)]

    # compute

    # output
    for K in Ks:
        for A in As:
            if A <= K:
                K += 1
        print(K)


if __name__ == '__main__':
    main()
