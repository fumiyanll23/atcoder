def main():
    # input
    x1, y1, x2, y2 = map(int, input().split())

    # compute
    rot = [[0, 1], [-1, 0]]
    diff_x, diff_y = x1-x2, y1-y2
    x3, y3 = x2+rot[0][0]*diff_x+rot[0][1]*diff_y, y2+rot[1][0]*diff_x+rot[1][1]*diff_y
    rot = [[0,-1], [1,0]]
    diff_x, diff_y = x2-x1, y2-y1
    x4, y4 = x1+rot[0][0]*diff_x+rot[0][1]*diff_y, y1+rot[1][0]*diff_x+rot[1][1]*diff_y

    # output
    print(x3, y3, x4, y4)


if __name__ == '__main__':
    main()
