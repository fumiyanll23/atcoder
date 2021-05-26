from math import ceil

def main():
    # input
    N, M = map(int, input().split())
    As = [*map(int, input().split())]

    # compute
    As.sort()
    As = [0] + As + [N+1]
    if N == M:
        print(0)
        exit()
    cnts = []
    for i in range(1,len(As)):
        if As[i] != As[i-1]+1:
            cnts.append(As[i]-As[i-1]-1)
    k = min(cnts)
    ans = 0
    for cnt in cnts:
        ans += ceil(cnt / k)

    # output
    print(ans)


if __name__ == '__main__':
    main()
