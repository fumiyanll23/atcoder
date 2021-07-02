from math import gcd
from functools import reduce

def my_gcd(*xs: list) -> int:
    return reduce(gcd, xs)

def main():
    # input
    A, B, C = map(int, input().split())

    # compute
    g = my_gcd(A, B, C)

    # output
    print(A//g + B//g + C//g - 3)


if __name__ == '__main__':
    main()
