def main():
    # input
    N = int(input())
    ss = [int(input()) for _ in range(N)]

    # compute
    ans = sum(ss)
    for s in sorted(ss):
        if ans%10==0 and s%10!=0:
            ans -= s

    # output
    if ans%10 == 0:
        print(0)
    else:
        print(ans)


if __name__ == '__main__':
    main()
