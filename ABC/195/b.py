def main():
    # input
    A, B, W = map(int, input().split())

    # compute
    W *= 1000
    cnt_min, cnt_max = 10**10, 0
    for i in range(1, 10**6+1):
        if A*i <= W <= B*i:
            cnt_min = min(cnt_min, i)
            cnt_max = max(cnt_max, i)

    # output
    if cnt_max == 0:
        print('UNSATISFIABLE')
    else:
        print(cnt_min, cnt_max)


if __name__ == '__main__':
    main()
