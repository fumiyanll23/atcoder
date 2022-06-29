def main():
    # input
    N = int(input())

    # compute
    ans = 1
    while ans*2 <= N:
        ans *= 2

    # output
    print(ans)


if __name__ == '__main__':
    main()
