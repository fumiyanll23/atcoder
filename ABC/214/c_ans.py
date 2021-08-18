def main():
    # input
    N = int(input())
    Ss = [*map(int, input().split())]
    Ts = [*map(int, input().split())]

    # compute
    for i in range(2*N):
        Ts[(i+1)%N] = min(Ts[(i+1)%N], Ts[i%N]+Ss[i%N])

    # output
    print(Ss)
    print(Ts)
    for ans in Ts:
        print(ans)


if __name__ == '__main__':
    main()
