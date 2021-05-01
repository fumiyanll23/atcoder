def main():
    # input
    N = int(input())
    As = [0] * N
    Bs = [0] * N
    Cs = [0] * N
    Ds = [0] * N
    Es = [0] * N
    for i in range(N):
        As[i], Bs[i], Cs[i], Ds[i], Es[i] = map(int, input().split())

    # compute

    # output
    print()
    print(max(As), max(Bs), max(Cs), max(Ds), max(Es))
    print(min(max(As), max(Bs), max(Cs), max(Ds), max(Es)))


if __name__ == '__main__':
    main()
