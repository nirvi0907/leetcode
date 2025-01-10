class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        1,3-1
        1,2
        '''
        rank = [0 for node in range(len(edges))]
        parent = [node for node in range(len(edges))]

        def find(node):
            cur = node
            while parent[cur]!=cur:
                cur = parent[cur]
            return cur

        def union(src, dst):
            parent_src = find(src)
            parent_dst = find(dst)
            if parent_src==parent_dst:
                return False
            if rank[parent_src]>=rank[parent_dst]:
                rank[parent_src]+=1
                parent[parent_dst] = parent_src
            elif rank[parent_src]<rank[parent_dst]:
                rank[parent_dst]+=1
                parent[parent_src] = parent_dst
            return True

        for src, dst in edges:
            if not union(src-1, dst-1):
                return [src, dst]
        return []