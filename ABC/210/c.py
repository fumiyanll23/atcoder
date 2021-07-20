from collections import defaultdict

def main():
    # input
    N, K = map(int, input().split())
    cs = [*map(int, input().split())]

    # compute
    ddict = defaultdict(int)
    for i in range(K):
        ddict[cs[i]] += 1
    ans = len(ddict)
    for i in range(N-K):
        ddict[cs[i]] -= 1
        if ddict[cs[i]] == 0:
            del ddict[cs[i]]
        ddict[cs[i+K]] += 1
        ans = max(ans, len(ddict))

    # output
    print(ans)


if __name__ == '__main__':
    main()
