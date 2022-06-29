def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    ans = 0
    sum_As = sum(As)
    for i in range(N):
        ans += (N-1)*As[i]**2 - 2*As[i]*(sum_As-As[i])
        sum_As -= As[i]

    # output
    print(ans)

if __name__ == '__main__':
    main()
