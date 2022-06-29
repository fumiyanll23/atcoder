def main():
    # input
    ABCs = list(map(int, input().split()))

    # compute
    cnt = 0
    while not(ABCs[0] == ABCs[1] == ABCs[2]):
        cnt += 1
        ABCs.sort()
        A, B, C = ABCs
        if C-A==1 or C-B==1:
            A += 1
            B += 1
        else:
            A += 2
        ABCs = [A, B, C]

    # output
    print(cnt)

if __name__ == '__main__':
    main()
