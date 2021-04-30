def main():
    # input
    N, M = map(int, input().split())
    pSs = [list(input().split()) for _ in range(M)]

    # compute
    pena =  0
    acs = [False] * N
    was = [0] * N
    for p,s in pSs:
        num = int(p)-1
        if s == 'AC':
            if not(acs[num]):
                acs[num] = True
                pena += was[num]
        else:
            was[num] += 1

    # output
    print(acs.count(True), pena)


if __name__ == '__main__':
    main()
