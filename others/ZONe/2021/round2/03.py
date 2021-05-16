def main():
    # input
    N, M = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(M)]

    # compute
    digs = [0] * N
    for ab in ABs:
        digs[ab[0]] += 1
        digs[ab[1]] += 1
    ans = []
    for _ in range(3):
        print(digs)
        dig_max = max(digs)
        print(f'dig_max = {dig_max}')
        dig_max_ind = digs.index(dig_max)
        print(f'dig_max_ind = {dig_max_ind}')
        ans.append(dig_max_ind)
        ## remove (earliest) vertex which has the maximam of digree
        digs[dig_max_ind] = 0
        for ab in ABs:
            if ab[0] == dig_max_ind:
                digs[ab[1]] -= 1
            elif ab[1] == dig_max_ind:
                digs[ab[0]] -= 1

    # output
    print(*list(sorted(ans)))


if __name__ == '__main__':
    main()
