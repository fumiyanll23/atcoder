from math import factorial

def main():
    # input
    P = int(input())

    # compute
    ans = 0
    for i in reversed(range(1, 11)):
        tmp_cnt = 0
        if factorial(i) <= P:
            tmp_cnt = P // factorial(i)
            P -= factorial(i) * tmp_cnt
            ans += tmp_cnt

    # output
    print(ans)


if __name__ == '__main__':
    main()
