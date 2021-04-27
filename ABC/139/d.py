def main():
    # input
    N = int(input())

    # compute
    if N == 1:
        ans = 0
    elif N%2 == 0:
        n = N // 2
        ans = n*(n+1)//2 + (n-1)
    else:
        n = N//2 - 1
        ans =

    # output
    print(ans)


if __name__ == '__main__':
    main()
