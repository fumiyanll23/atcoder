from math import gcd
from functools import reduce

def my_gcd(*xs: list) -> int:
    return reduce(gcd, xs)


def my_lcm_base(x: int, y: int) -> int:
    return (x*y) // gcd(x,y)


def my_lcm(*xs: list) -> int:
    return reduce(my_lcm_base, xs, 1)


def f(m: int, xs: list) -> int:
    ans = 0
    for x in xs:
        ans += m%x
    return ans


def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute

    # output
    print(f(my_lcm(*As)-1, As))


if __name__ == '__main__':
    main()
