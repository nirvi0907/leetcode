https://leetcode.com/problems/largest-submatrix-with-rearrangements/
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix) # num rows
        n = len(matrix[0]) # num cols
        # The height of a column of 1's at a specific index
        heights = matrix[0].copy()
        maxArea = heights.count(1)
        for ri in range(1, m):
            # Increase or reset height of the column
            for ci in range(n):
                if matrix[ri][ci] == 1:
                    heights[ci] += 1
                else:
                    heights[ci] = 0
            # Bring columns into a "triangle" form, with descending values
            sortedHeights = sorted(heights.copy(), reverse=True)
            # Check the area of all possible rectangles inside the imagined triangle
            for i in range(n):
                area = sortedHeights[i] * (i+1)
                if area > maxArea:
                    maxArea = area
        return maxArea
