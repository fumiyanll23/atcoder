# UnionFindTree
class UnionFind:
    def __init__(self, n):
        self.p = [-1] * n  # parent
        self.r = [1] * n  # rank
    def find(self, x):
        if self.p[x] == -1:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.r[x] > self.r[y]:
            x, y = y, x
        if self.r[x] == self.r[y]:
            self.r[y] += 1
        self.p[x] = y
    def same(self, x, y):
        return self.find(x) == self.find(y)

# 使用例
def main():
    # input
    N, M = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(M)]

    # compute
    uf = UnionFind(N)
    for AB in ABs:
        a, b = AB
        uf.unite(a-1, b-1)
    ans = 0
    for i in range(N):
        for j in range(N):
            if uf.same(i, j):
                ans += 1


    # output
    print(ans)


if __name__ == '__main__':
    main()
