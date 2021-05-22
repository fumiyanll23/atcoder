def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    Cs = list(map(int, input().split()))

    # compute
    Acounts = [0] * N
    for a in As:
        Acounts[a-1] += 1
    cnt = 0
    for c in Cs:
        cnt += Acounts[Bs[c-1]-1]

    # output
    print(cnt)


if __name__ == '__main__':
    main()
