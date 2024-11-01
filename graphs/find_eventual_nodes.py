class Solution:
    # def eventualSafeNodes(self, graph):
    #     N = len(graph)
    #     dp = [-1] * N
    #     def dfs(x):
    #         if dp[x] != -1: return dp[x]
    #         dp[x] = 0
    #         for i in graph[x]:
    #             if dfs(i) == 0:
    #                 return 0
    #         dp[x] = 1
    #         return 1
    #     return [i for i in range(N) if dfs(i)]

    #     class Solution:

    #topo sorting
    '''
    if we move from terminal nodes (opp direction), we can keep deducting outdegree nodes,
    if outdegree gets to 0, that means its not part of cycle hence its safe node, 

    '''

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #we start from terminal node, then find safe nodes, since we wanna start from temrinal nodes, we switch the directions
            n=len(graph)
            indegree=[0]*(n)
            adj=[[]for _ in range(n)]
            for u in range(n):
                for v in graph[u]:
                    adj[v].append(u)
                    indegree[u]+=1

            
            queue=deque()
            #get terminal ndoes
            for v in range(n):
                if indegree[v]==0:
                    queue.append(v)
            print(queue)
            ans=[]
            #from terminal nodes we find next safe nodes, then next safe nodes etc
            while queue:
                u=queue.popleft()
                ans.append(u)
                for v in adj[u]:
                    indegree[v]-=1
                    #if we found safe node, add in queue
                    if indegree[v]==0:
                        print(v)
                        queue.append(v)
            return sorted(ans)
            
                