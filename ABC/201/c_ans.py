from itertools import product

def main():
    # input
    S = input()

    # compute
    numbers = []
    requires = []
    for i,s in enumerate(S):
        if s != 'x':
            numbers.append(i)
        if s == 'o':
            requires.append(i)
    cnt = 0
    for password in product(numbers, repeat=4):
        if set(password) >= set(requires):
            cnt += 1

    # output
    print(cnt)


if __name__ == '__main__':
    main()
