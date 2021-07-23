def main():
    # input
    N = int(input())
    As = [int(input()) for _ in range(N)]

    # compute
    Amax = sorted(As)[-1]
    Asemimax = sorted(As)[-2]
    cnt = As.count(Amax)

    # output
    for A in As:
        if A==Amax and cnt==1:
            print(Asemimax)
        else:
            print(Amax)


if __name__ == '__main__':
    main()
