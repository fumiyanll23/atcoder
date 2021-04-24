def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    # compute
    As_max = max(As)
    Bs_min = min(Bs)
    if As_max <= Bs_min:
        cnt = Bs_min-As_max+1
    else:
        cnt = 0

    # output
    print(cnt)


if __name__ == '__main__':
    main()
