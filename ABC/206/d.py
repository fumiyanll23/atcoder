def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    As1, As2 = As[:N//2], [*reversed(As[(N+1)//2:])]
    ans = set()
    for A1,A2 in zip(As1,As2):
        if A1 != A2:
            ans.add(A1)
            ans.add(A2)

    # output
    if ans == set():
        print(0)
    else:
        print(len(ans)-1)


if __name__ == '__main__':
    main()
