from math import ceil

def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute

    # output
    print(ceil(sum(As) / sum([A != 0 for A in As])))


if __name__ == '__main__':
    main()
