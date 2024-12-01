class Solution:
    #time - E=V**2 BECAUSE WORST CASE every vertex is connected to every other vertex
    #now worst case every edge in heap - logV**2 to pop and push
    #so overall time - E(worst case all neighbors)*log(V**2)
    #approx - E(log V)
    #ques asks to get the min distance to reach farthest node'
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_lst = defaultdict(list)
        for src, dst, cost in times:
            adj_lst[src].append([dst, cost])

        heap = [(0, k)]
        visit = set()
        while heap:
            #we get the next min cumulative cost
            min_cost, node = heapq.heappop(heap) #1
            visit.add(node) #2
            if len(visit)==n:
                return min_cost
            for dst, dst_cost in adj_lst[node]:
                if dst not in visit:
                    heapq.heappush(heap, (min_cost+dst_cost, dst )) #1,2,1
        return -1