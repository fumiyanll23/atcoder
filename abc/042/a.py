from abc import ABC


def main():
    # input
    ABCs = [*map(int, input().split())]

    # compute

    # output
    print('YES' if ABCs.count(5)==2 and ABCs.count(7)==1 else 'NO')


if __name__ == '__main__':
    main()
