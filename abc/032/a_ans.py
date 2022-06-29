from math import gcd, ceil

def lcm(x: int, y: int) -> int:
    return x*y // gcd(x,y)

def main():
    # input
    a = int(input())
    b = int(input())
    n = int(input())

    # compute

    # output
    print(lcm(a,b) * ceil(n/lcm(a,b)))


if __name__ == '__main__':
    main()
