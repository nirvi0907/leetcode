class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        #we need to check this first since we cant move back fourth from first cell as no prev cell
        #if this is false, we are always blocked
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        heap = [(0, 0, 0)]
        rows, cols = len(grid), len(grid[0])

        def is_valid(dx, dy):
            if 0<=dx<rows and 0<=dy<cols and grid[dx][dy]!=-1:
                return True
            return False
        
        while heap:
            cost, row, col = heapq.heappop(heap)
            if row==rows-1 and col==cols-1:
                return cost
            #could be same cell has duplicate entries, if first time its visited already, then subsequent dont visit
            if grid[row][col]==-1:
                continue
            grid[row][col] = -1
            for dr, dc in [[-1,0], [0,-1], [0,1], [1,0]]:
                dx, dy = row + dr, col + dc
                if is_valid(dx, dy):
                    if cost+1>=grid[dx][dy]:
                        heapq.heappush(heap, (cost+1, dx, dy))
                    else:
                        diff = grid[dx][dy]-cost
                        if diff%2:
                            heapq.heappush(heap, (grid[dx][dy], dx, dy))
                        else:
                            heapq.heappush(heap, (grid[dx][dy]+1, dx, dy))
        return -1