def main():
    # input
    N = int(input())
    ALPHABET = 26

    # compute
    ans = ''
    while N:
        N -= 1
        ans += chr(ord('a') + N%ALPHABET)
        N //= 26

    # output
    print(ans[::-1])


if __name__ == '__main__':
    main()
