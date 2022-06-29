def main():
    # input
    N = int(input())

    # compute
    mod = 10**9 + 7
    power = 1
    for i in range(1, N+1):
        power = power * i % mod

    # output
    print(power)


if __name__ == '__main__':
    main()
