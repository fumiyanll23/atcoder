def main():
    # input
    A, B, C = map(int, input().split())

    # compute

    # output
    if B>=A>=C or C>=A>=B:
        print('A')
    elif A>=B>=C or C>=B>=A:
        print('B')
    else:
        print('C')



if __name__ == '__main__':
    main()
