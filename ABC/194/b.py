def main():
    # input
    N = int(input())
    As = [0 for _ in range(N)]
    Bs = [0 for _ in range(N)]
    for i in range(N):
        As[i], Bs[i] = map(int, input().split())

    # compute
    ans = []

    for i in range(N):
        for j in range(N):
            if i != j:
                ans.append(max(As[i], Bs[j]))
            else:
                ans.append(As[i] + Bs[j])

    # output
    print(min(ans))


if __name__ == '__main__':
    main()
