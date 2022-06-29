def main():
    # input
    css = [[*map(int, input().split())] for _ in range(3)]

    # compute
    for a1 in range(101):
        for a2 in range(101):
            for a3 in range(101):
                As = [a1, a2, a3]
                Bs = [css[0][0]-a1, css[1][1]-a2, css[2][2]-a3]
                flag = True
                for i in range(3):
                    for j in range(3):
                        if As[i]+Bs[j] != css[i][j]:
                            flag = False
                if flag:
                    print('Yes')
                    exit()

    # output
    print('No')


if __name__ == '__main__':
    main()
