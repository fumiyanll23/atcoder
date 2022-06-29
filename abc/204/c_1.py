import networkx as nx

def main():
    # input
    N, M = map(int, input().split())
    ABs = [[*map(int, input().split())] for _ in range(M)]

    # compute
    G = nx.DiGraph()
    for i in range(N):
        G.add_node(i)
    for a,b in ABs:
        G.add_edge(a-1, b-1)

    def set_univisited(G) -> list:
        vstates = []
        for _ in range(len(G)):
            vstates.append(None)

        return vstates

    states = set_univisited(G)

    def DFS(G, start):
        states[start] = True
        for u in G[start]:
            if not states[u]:
                DFS(G, u)

    # output
    print(G.nodes())
    print(G.edges())


if __name__ == '__main__':
    main()
