from math import factorial

def main():
    # input
    P = int(input())

    # compute
    ans = 0
    for i in reversed(range(1, 11)):
        while factorial(i) <= P:
            P -= factorial(i)
            ans += 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
