class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for start_idx in range(len(bombs)):
            center_x, center_y, r = bombs[start_idx]
            for end_idx in range(len(bombs)):
                if start_idx!=end_idx:
                    x,y,_ = bombs[end_idx]
                    if ((center_x-x)**2 + (center_y-y)**2) <=r**2:
                        adj_list[start_idx].append(end_idx)
        
        def detonate(idx):
            visit = set()
            queue = deque([idx])
            visit.add(idx)
            det = 0
            while queue:
                node = queue.popleft()
                
                det+=1
                for neigh in adj_list[node]:
                    if neigh not in visit:
                        visit.add(neigh)
                        queue.append(neigh)
            return det
        
        max_det_bombs = 0
        for idx in range(len(bombs)):
            
            max_det_bombs = max(max_det_bombs, detonate(idx))

        return max_det_bombs


