def main():
    # input
    ABCs = list(map(int, input().split()))

    # compute
    s, M = sum(ABCs), max(ABCs)
    if s%2 == 3*M%2:
        print((3*M-s)//2)
    else:
        print((3*(M+1)-s)//2)

    # output

if __name__ == '__main__':
    main()
