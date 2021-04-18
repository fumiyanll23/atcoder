def main():
    # input
    N, K = map(int, input().split())
    Ss = [input() for _ in range(N)]

    # compute
    S_dict = {}
    for i in Ss:
        if i in S_dict:
            S_dict[i] += 1
        else:
            S_dict[i] = 1

    # output
    ans_dict = sorted(S_dict, reverse=True)
    print(ans_dict)
    if ans_dict[0]==ans_dict[1] or ans_dict[1]==ans_dict[2]:
        print('AMBIGUOUS')
    else:
        print(ans_dict[1])


if __name__ == '__main__':
    main()
