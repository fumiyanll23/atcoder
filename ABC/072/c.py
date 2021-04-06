def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    As.sort()
    if len(As) == 1:
        print(1)
        exit()
    else:
        Bs = []
        for i in range(N-1):
            Bs.append(As[i+1]-As[i])

    # output
    print(Bs.count(1))


if __name__ == '__main__':
    main()
