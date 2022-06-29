def main():
    # input
    N, K = map(int, input().split())
    ps = list(map(int, input().split()))

    # compute
    es = [0] * N
    for i,p in enumerate(ps):
        es[i] = (p+1) / 2
    psum = sum(es[:K])
    ans = psum
    for i in range(N-K):
        psum = psum - es[i] + es[i+K]
        ans = max(ans, psum)

    # output
    print(ans)


if __name__ == '__main__':
    main()
