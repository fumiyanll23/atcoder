def main():
    # input
    x1, y1, x2, y2 = map(int, input().split())

    # compute
    diff_x, diff_y = x2-x1, y2-y1

    # output
    print(x2-diff_y, y2+diff_x, x1-diff_y, y1+diff_x)


if __name__ == '__main__':
    main()
