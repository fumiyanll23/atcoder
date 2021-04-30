def main():
    # input
    H, W = map(int, input().split())
    Ss = [input() for _ in range(H)]

    # compute
    for i in range(H):
        for j in range(W):
            k, cnts = -1, []
            if Ss[i][j] == '.':
                cnts.append(0)
                k += 1
                if j+1 != W:
                    if Ss[i][j+1] == '#':
                        cnts[k] += 1
                    if i-1 != -1:
                        if Ss[i-1][j+1] == '#':
                            cnts[k] += 1
                    if i+1 != H:
                        if Ss[i+1][j+1] == '#':
                            cnts[k] += 1
                if i+1 != H:
                    if Ss[i+1][j] == '#':
                        cnts[k] += 1
                if j-1 != -1:
                    if Ss[i][j-1] == '#':
                        cnts[k] += 1
                    if i-1 != -1:
                        if Ss[i-1][j-1] == '#':
                            cnts[k] += 1
                    if i+1 != H:
                        if Ss[i+1][j-1] == '#':
                            cnts[k] += 1
                if i-1 != -1:
                    if Ss[i-1][j] == '#':
                        cnts[k] += 1
            else:
                cnts.append('#')
                k += 1
            print(*cnts, end='')
        print()

    # output


if __name__ == '__main__':
    main()
