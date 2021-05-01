from collections import deque

def main():
    # input
    S = input()

    # compute
    T = deque([])
    flag = False
    for s in S:
        if s == 'R':
            flag = not(flag)
        else:
            if flag:
                T.appendleft(s)
                if len(T)>=2 and T[0]==T[1]:
                    T.popleft()
                    T.popleft()
            else:
                T.append(s)
                if len(T)>=2 and T[-2]==T[-1]:
                    T.pop()
                    T.pop()
    if flag:
        T.reverse()

    # output
    print(''.join(list(T)))


if __name__ == '__main__':
    main()
