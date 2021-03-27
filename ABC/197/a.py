# ABC197A - Rotate

def main():
    # input
    S = str(input())

    # compute
    ans = ''
    ans += S[1] + S[2] + S[0]

    # output
    print(ans)


if __name__ == '__main__':
    main()
