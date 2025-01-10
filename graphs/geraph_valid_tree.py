class DSU:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def findParent(self, node) -> int:
        p = self.parent[node]
        while p != self.parent[p]:
            # path compression
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, node_a, node_b) -> bool:
        parent_a, parent_b = self.findParent(node_a), self.findParent(node_b)
        if parent_a == parent_b:
            return False

        rank_a, rank_b = self.rank[parent_a], self.rank[parent_b]
        if rank_a >= rank_b:
            self.parent[parent_b] = parent_a
            self.rank[parent_a] += rank_b
        else:
            self.parent[parent_a] = parent_b
            self.rank[parent_b] += rank_a
        return True


class Solution:
    # Union Find
    # O(v + e) time | O(v) space
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        v, e = n, len(edges)
        if v - 1 != e:
            return False

        dsu = DSU(v)
        for i, j in edges:
            if not dsu.union(i, j):
                return False

        # we know there's no self edges or repeated edges
        # so we don't need to keep track of any how edges
        # the dsu was able to join, so we for sure
        # that a valid graph tree can be created
        return True