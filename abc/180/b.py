from math import sqrt

def main():
    # input
    N = int(input())
    xs = [*map(int, input().split())]

    # compute

    # output
    print(sum([abs(x) for x in xs]))
    print(sqrt(sum([x*x for x in xs])))
    print(max([abs(x) for x in xs]))


if __name__ == '__main__':
    main()
