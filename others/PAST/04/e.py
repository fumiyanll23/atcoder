from itertools import permutations

def main():
    # input
    N = int(input())
    S = input()

    # compute
    T_like = list(permutations(S,N))
    for i in T_like:
        T = ''.join(i)
        if T!=S and reversed(T)!=S:
            print(T)
            exit()

    # output
    print('None')


if __name__ == '__main__':
    main()
