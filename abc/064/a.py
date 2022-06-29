def main():
    # input
    r, g, b = map(int, input().split())

    # compute

    # output
    print('YES' if (r*100+g*10+b)%4==0 else 'NO')


if __name__ == '__main__':
    main()
