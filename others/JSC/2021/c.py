from math import gcd

def main():
    # input
    A, B = map(int, input().split())

    # compute
    max_like = 0
    for i in range(A, B):
        for j in range(i+1, B+1):
            gcd_like = gcd(i, j)
            if gcd_like > max_like:
                max_like = gcd_like

    # output
    print(max_like)

if __name__ == '__main__':
    main()
