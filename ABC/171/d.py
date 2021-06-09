def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]
    Q = int(input())
    BCs = [[*map(int, input().split())] for _ in range(Q)]

    # compute
    cnts = [0] * 10**5
    for A in As:
        cnts[A-1] += 1
    ans = sum(As)
    for B,C in BCs:
        ans += (C-B) * cnts[B-1]
        cnts[C-1] += cnts[B-1]
        cnts[B-1] = 0
        print(ans)

    # output


if __name__ == '__main__':
    main()
