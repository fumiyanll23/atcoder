def main():
    # input
    H, W = map(int, input().split())

    # compute
    h = (H+1) // 2
    w = (W+1) // 2

    # output
    print(h * w)


if __name__ == '__main__':
    main()
