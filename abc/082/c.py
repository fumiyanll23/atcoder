from collections import defaultdict

def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    ddict = defaultdict(int)
    for A in As:
        ddict[A] += 1
    ans = 0
    for k, v in ddict.items():
        if k <= v:
            ans += v - k
        else:
            ans += v

    # output
    print(ans)


if __name__ == '__main__':
    main()
