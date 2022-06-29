def main():
    # input
    N = int(input())
    ds = [*map(int, input().split())]

    # compute
    ds.sort()

    # output
    print(ds[N//2] - ds[N//2-1])


if __name__ == '__main__':
    main()
