def main():
    # input
    N, M = map(int, input().split())
    ss = [input() for _ in range(N)]

    # compute
    for i in range(N):
        row = ''
        for j in range(M):
            dot = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0<=i+dx<N and 0<=j+dy<M and ss[i+dx][j+dy]=='#':
                        dot += 1
            row += str(dot)
        print(row)

    # output


if __name__ == '__main__':
    main()
