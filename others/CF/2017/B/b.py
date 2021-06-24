from collections import defaultdict

def main():
    # input
    N = int(input())
    Ds = [*map(int, input().split())]
    M = int(input())
    Ts = [*map(int, input().split())]

    # compute
    D_dict = defaultdict(int)
    T_dict = defaultdict(int)
    flag = True
    for D in Ds:
        D_dict[D] += 1
    for T in Ts:
        T_dict[T] += 1
    for T_key in T_dict:
        if D_dict[T_key] >= T_dict[T_key]:
            pass
        else:
            flag = False

    # output
    if flag:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
