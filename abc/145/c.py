from itertools import permutations
from math import sqrt

def main():
    # input
    N = int(input())
    xyss = [list(map(int, input().split())) for _ in range(N)]

    # compute
    d_sum = 0
    patterns = list(permutations(range(N), N))
    n = len(patterns)
    for i in range(n):
        for j in range(N-1):
            d_sum += sqrt((xyss[patterns[i][j]][0]-xyss[patterns[i][j+1]][0])**2 + (xyss[patterns[i][j]][1]-xyss[patterns[i][j+1]][1])**2)

    # output
    print(d_sum/n)


if __name__ == '__main__':
    main()
