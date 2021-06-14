from math import gcd
from functools import reduce

def my_gcd(*numbers) -> int:
    return reduce(gcd, numbers)


def main():
    # input
    N, X = map(int, input().split())
    xs = [*map(int, input().split())]

    # compute
    xs_diff = [0] * N
    for i,x in enumerate(xs):
        xs_diff[i] = abs(x - X)

    # output
    print(my_gcd(*xs_diff))


if __name__ == '__main__':
    main()
