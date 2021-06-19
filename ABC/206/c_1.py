def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    cnt = 0
    for Ai in As:
        for Aj in As:
            if Ai != Aj:
                cnt += 1

    # output
    print(cnt // 2)


if __name__ == '__main__':
    main()
