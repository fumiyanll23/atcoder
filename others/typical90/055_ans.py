def main():
    # input
    N, P, Q = map(int, input().split())
    As = [*map(int, input().split())]

    # compute
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    for m in range(l+1, N):
                        tmp_prd = (
                            (
                                (
                                    As[i]*As[j] % P
                                ) * As[k] % P
                            ) * As[l] % P
                        ) * As[m] % P
                        if tmp_prd == Q:
                            ans += 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
