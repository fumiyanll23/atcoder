from collections import defaultdict

def main():
    # input
    N = int(input())
    ss = [input() for _ in range(N)]

    # compute
    for i in range(N):
        ss[i] = ''.join(sorted(ss[i]))
    ddict = defaultdict(int)
    for s in ss:
        ddict[s] += 1
    ans = 0
    for key, value in ddict.items():
        ans += value*(value-1)//2

    # output
    print(ans)


if __name__ == '__main__':
    main()
