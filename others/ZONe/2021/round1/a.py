def main():
    # input
    S = input()

    # compute
    cnt = 0
    for i in range(9):
        if S[i:i+4] == 'ZONe':
            cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
