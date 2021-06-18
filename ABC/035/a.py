def main():
    # input
    W, H = map(int, input().split())

    # compute

    # output
    if H/W == 0.75:
        print('4:3')
    else:
        print('16:9')


if __name__ == '__main__':
    main()
