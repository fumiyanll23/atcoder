from codecs import decode

def main():
    # input
    N = 31
    Ss = [input() for _ in range(N)]

    # compute

    # output
    # print()
    for s in Ss:
        print(decode(s, 'rot13'))


if __name__ == '__main__':
    main()
