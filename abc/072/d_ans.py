def main():
    # input
    N = int(input())
    ps = list(map(int, input().split()))

    # compute
    cnt = 0
    for i in range(N-1):
        if i+1 == ps[i]:
            ps[i], ps[i+1] = ps[i+1], ps[i]
            cnt += 1
    if N == ps[-1]:
        cnt += 1

    # output
    print(cnt)

if __name__ == '__main__':
    main()
