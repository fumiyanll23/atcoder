def main():
    # input
    ABCs = list(map(int, input().split()))

    # compute
    A, B, C = reversed(sorted(ABCs))

    # output
    if (A-B)%2==0 and (A-C)%2==0:
        print((2*A-B-C)//2)
    else:
        if A-B==1 or A-C==1:
            print((2*A-B-C)//2)
        else:
            print((2*A-B-C)//2+1)

if __name__ == '__main__':
    main()
