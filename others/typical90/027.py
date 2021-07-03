def main():
    # input
    N = int(input())
    Ss = [input() for _ in range(N)]

    # compute
    set_user = set()
    for i, S in enumerate(Ss):
        if S not in set_user:
            print(i+1)
            set_user.add(S)

    # output


if __name__ == '__main__':
    main()
