def main():
    # input
    N = int(input())
    S = input()

    # compute
    slimes = S[0]
    for s in S:
        if s != slimes[-1]:
            slimes += s

    # output
    print(len(slimes))


if __name__ == '__main__':
    main()
