def main():
    # input
    S = [*input()]

    # compute
    S_set = set(S)

    # output
    if len(S_set) == len(S):
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()
