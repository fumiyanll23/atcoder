def main():
    # input
    N, M = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(M)]

    # compute
    adj = set(max(AB) for AB in ABs if min(AB) == 1)
    flag = any(min(AB) in adj for AB in ABs if max(AB) == N)

    # output
    if flag:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    main()
