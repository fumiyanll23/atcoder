def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    cnt, odd = 0, 0
    while True:
        for i in As:
            if i%2 == 1:
                i *= 3
                odd += 1
                print('odd', odd)
                if odd == 2:
                    break
            else:
                i /= 2
        cnt += 1
        print('cnt', cnt)

    # output
    print(cnt)

if __name__ == '__main__':
    main()
