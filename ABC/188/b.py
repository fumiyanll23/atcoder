def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]
    Bs = [*map(int, input().split())]

    # compute
    dot_prd = 0
    for A, B in zip(As, Bs):
        dot_prd += A * B

    # output
    if dot_prd == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
