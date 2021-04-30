def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    # compute
    cnts = [0] * N
    for i in range(N):
        if i == 0:
            cnts[i] += As[i] + sum(Bs[i:])
        elif i == N-1:
            cnts[i] += sum(As[:i]) + Bs[i]
        else:
            cnts[i] += sum(As[:i+1]) + sum(Bs[i:])

    # output
    print(max(cnts))


if __name__ == '__main__':
    main()
