def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    ans = 0
    for A in As:
        if A <= 10:
            pass
        else:
            ans += A - 10

    # output
    print(ans)


if __name__ == '__main__':
    main()
