class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#there wont be more than 2 answers becasuse if we try to  keep tree in stargight line, more left or right we go, 
#it becomes unablanced and lead to more heigh, in middle the height is least,
#so either in middle there will be one node or 2 nodes,  more than that not possible
#if we say middle we have 3 nodes, then between 3 nodes , center one will have a diff height than other 2 right? 
        # edge cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves