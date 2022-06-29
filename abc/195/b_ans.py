from math import floor, ceil

def main():
    # input
    A, B, W = map(int, input().split())

    # compute
    W *= 1000
    upper = int(floor(W/A))
    lower = int(ceil(W/B))

    # output
    if lower > upper:
        print('UNSATISFIABLE')
    else:
        print(lower, upper)


if __name__ == '__main__':
    main()
