def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    cnt = 0
    for a in As:
        while a%2 == 0:
            a //= 2
            cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
