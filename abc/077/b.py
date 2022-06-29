def main():
    # input
    N = int(input())

    # compute
    ans = 1
    while ans**2 <= N:
        ans += 1

    # output
    print((ans-1)**2)


if __name__ == '__main__':
    main()
