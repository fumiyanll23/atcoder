def main():
    # input
    A, B = map(int, input().split())

    # compute
    for gcd_like in range(B, 0, -1):
        if (A+gcd_like-1)//gcd_like < B//gcd_like:
            exit(print(gcd_like))

    # output


if __name__ == '__main__':
    main()
