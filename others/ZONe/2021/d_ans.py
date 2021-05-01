from collections import deque

def main():
    # input
    S = input()

    # compute
    T = deque()
    flag = False
    for s in S:
        if s == 'R':
            flag = not(flag)
        elif flag:
            if T and T[0]==s:
                T.popleft()
            else:
                T.appendleft(s)
        else:
            if T and T[-1]==s:
                T.pop()
            else:
                T.append(s)
    if flag:
        T.reverse()

    # output
    print(''.join(T))


if __name__ == '__main__':
    main()
