from itertools import permutations

def main():
    # input
    A, B, K = map(int, input().split())

    # compute
    ABs = 'a'*A + 'b'*B

    # output
    print(''.join(list(set(permutations(ABs, A+B)))[K-1]))


if __name__ == '__main__':
    main()
