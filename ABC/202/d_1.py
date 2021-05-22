from math import factorial

def main():
    # input
    A, B, K = map(int, input().split())

    # compute
    n = factorial(A+B) // factorial(A) // factorial(B)
    s = ''
    while n//2 != 0:
        n //= 2
        if K <= n:
            s += 'a'
        else:
            s += 'b'

    # output
    print(s)


if __name__ == '__main__':
    main()
