def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    cnt = 0
    for i in range(N):
        while As[i]%2 == 0:
            As[i] //= 2
            cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
