class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodes_map = defaultdict(int)
        #since graph isnt connected
        for node in range(len(graph)):
            if nodes_map[node]:
                continue
            queue = deque()
            queue.append((node, -1))
            while queue:
                node, nodeset = queue.popleft()
                nodes_map[node] = nodeset
                for neigh in graph[node]:
                    if nodes_map[neigh]==nodeset:
                        return False
                    if nodes_map[neigh]:
                        continue
                    queue.append((neigh, nodeset*-1))
        return True
