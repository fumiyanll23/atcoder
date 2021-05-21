def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    cnt = 0
    for i,a in enumerate(As):
        if As[a-1] == i+1:
            cnt += 1

    # output
    print(cnt // 2)


if __name__ == '__main__':
    main()
