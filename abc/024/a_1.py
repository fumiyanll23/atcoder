def main():
    # input
    A, B, C, K = map(int, input().split())
    S, T = map(int, input().split())

    # compute

    # output
    print(A*S+B*T if S+T<K else A*S+B*T-(S+T)*C)


if __name__ == '__main__':
    main()
