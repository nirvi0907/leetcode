import heapq
Dijkstra has O(|E| * log(|V|)) and Dijkstra is applied to each node (i.e. |V| times).
O(|V| * |E| * log(|V|)) = O(N^3 * log(N))

def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
	adj = build_graph(n, edges)

	min_city, min_reach = None, math.inf
	for node in range(n):
		reach = dijkstra(node, adj, distanceThreshold)
		if reach <= min_reach:
			min_city = node
			min_reach = reach
	return min_city
     

def build_graph(n, edges):
    adj = [[] for _ in range(n)]
    
    for source, dest, weight in edges:
        adj[source].append((dest, weight))
        adj[dest].append((source, weight))
    
    return adj


# return the reachability
def dijkstra(source, adj, distanceThreshold) -> int:
    # from source, it calcualtes shortest distance to every other node, 
    # and couting how many nodes have shortest distance from source within threshold
    n = len(adj)
    
    dest = [math.inf] * n
    dest[source] = 0
    
    visited = [0] * n
    
    pq = [(0, source)]
    
    while pq:
        node_dest, node = heapq.heappop(pq)
        visited[node] = 1
        
        for neigh, edge_weight in adj[node]:
            if visited[neigh] == 0:
                new_dest = node_dest + edge_weight
                if new_dest < dest[neigh]:
                    dest[neigh] = new_dest
                    heapq.heappush(pq, (new_dest, neigh))
    
    reach = 0
    for d in dest:
        if d <= distanceThreshold:
            reach += 1
    return reach

# ----------------------------------------------------------------------------------------/
#floyd
'''
we get the shortest diatance to every node
'''
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[math.inf] * n for _ in range(n)]

        for node in range(n):
            dist[node][node] = 0
        for source, dest, weight in edges:
            dist[source][dest] = weight
            dist[dest][source] = weight

        for pivot in range(n):
            for nodea in range(n):
                for nodeb in range(n):
                    trans_dist = dist[nodea][pivot] + dist[pivot][nodeb]
                    if trans_dist < dist[nodea][nodeb]:
                        dist[nodea][nodeb] = trans_dist
                        dist[nodeb][nodea] = trans_dist

        min_city, min_reach = None, math.inf
        for nodea in range(n):
            nodea_reach = 0
            for nodeb in range(n):
                if dist[nodea][nodeb] <= distanceThreshold:
                    nodea_reach += 1
            if nodea_reach <= min_reach:
                min_city = nodea
                min_reach = nodea_reach

        return min_city