from math import factorial

def main():
    # input
    P = int(input())

    # compute
    ans = 0
    for i in range(1, 11):
        res = P % factorial(i+1)
        ans += res // factorial(i)
        P -= res

    # output
    print(ans)


if __name__ == '__main__':
    main()
