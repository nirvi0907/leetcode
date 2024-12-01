class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # eulier paths problem says every edge is visited once from start node
        #meaning start nodes outdegree-indgeree ==1
        #end node indegree-outdegree==1 
                # graph represents adjacency list, inOutDeg tracks in/out degree difference
        graph = defaultdict(list)
        inOutDeg = defaultdict(int)

        # Build graph and count in/out degrees
        for start, end in pairs:
            graph[start].append(end)
            inOutDeg[start] += 1  # out-degree
            inOutDeg[end] -= 1    # in-degree

        # Find starting node 
        startNode = pairs[0][0] 
        for node in inOutDeg:
            if inOutDeg[node] == 1:
                startNode = node
                break

        path = []
        def dfs(curr):
            while graph[curr]:
                nextNode = graph[curr].pop()
                dfs(nextNode)
                #the first value is the edge to end node 
                path.append((curr, nextNode))

        dfs(startNode)
        return path[::-1]