def main():
    # input
    N, X = map(int, input().split())
    As = [*map(int, input().split())]

    # compute
    ans = []
    for A in As:
        if A != X:
            ans.append(A)

    # output
    print(*ans)


if __name__ == '__main__':
    main()
