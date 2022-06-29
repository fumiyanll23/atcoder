def main():
    # input
    N, X = map(int, input().split())
    As = [*map(int, input().split())]

    # compute

    # output
    print(' '.join([str(A) for A in As if A != X]))


if __name__ == '__main__':
    main()
