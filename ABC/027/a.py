def main():
    # input
    ls = [*map(int, input().split())]

    # compute

    # output
    for i in range(3):
        if ls[i-1] == ls[i]:
            print(ls[i-2])
            exit()

if __name__ == '__main__':
    main()
