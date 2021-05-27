def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    As.sort(reverse=True)
    psum = sum(As) - As[0]
    ans = 0
    for i in range(N-1):
        ans += (N-i-1)*As[i] - psum
        psum -= As[i+1]

    # output
    print(ans)


if __name__ == '__main__':
    main()
