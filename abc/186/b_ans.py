import numpy as np

def main():
    # input
    H, W = map(int, input().split())
    Ass = [[*map(int, input().split())] for _ in range(H)]

    # compute
    Ass = np.array(Ass)

    # output
    print(np.sum(Ass - np.min(Ass)))


if __name__ == '__main__':
    main()
