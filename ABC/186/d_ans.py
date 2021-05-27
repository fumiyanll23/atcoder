def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    As.sort()
    ans = 0
    for i,A in enumerate(As):
        ans += i*A - (N-i-1)*A

    # output
    print(ans)


if __name__ == '__main__':
    main()
