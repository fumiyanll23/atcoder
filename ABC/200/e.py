from itertools import product

def main():
    # input
    N, K = map(int, input().split())

    # compute

    # output
    print(list(product(range(N), repeat=3))[K-1])


if __name__ == '__main__':
    main()
