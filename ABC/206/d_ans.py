class UnionFind():
    def __init__(self, n: int):
        """Union Find

        Args:
            n (int): 全体の個数
        """
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int):
        """x番目の要素の親を持ってくる. < O(log N)"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int):
        """ x と y をくっつける"""
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int):
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int):
        """ x と y が同じグループかどうか"""
        return self.find(x) == self.find(y)

    def members(self, x: int):
        """ x と同じグループのやつを持ってくる"""
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """根となってるやつを持ってくる"""
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """グループの数"""
        return len(self.roots())

    def all_group_members(self):
        """全グループのメンバーを持ってくる"""
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(f'{r}: {self.members(r)}' for r in self.roots())


def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    uf = UnionFind(max(As)+1)
    for i in range((N+1)//2):
        uf.union(As[i], As[-i-1])
    ans = 0
    for r in uf.roots():
        ans += uf.size(r) - 1

    # output
    print(ans)


if __name__ == '__main__':
    main()
