def main():
    # input
    S = list(map(int, input()))
    K = int(input())

    # compute
    cnt = 0

    # output
    for s in S:
        if s == 1:
            cnt += 1
        else:
            if cnt == K:
                print(1)
                exit()
            else:
                print(s)
                exit()
    print(1)

if __name__ == '__main__':
    main()
