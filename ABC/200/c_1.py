from math import factorial

def combination(n: int, r: int) -> int:
    return factorial(n) // (factorial(n-r)*factorial(r))

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    cnts = [0] * 200
    for a in As:
        cnts[a%200] += 1
    ans = 0
    for cnt in cnts:
        if cnt >= 2:
            ans += combination(cnt, 2)

    # output
    print(ans)


if __name__ == '__main__':
    main()
