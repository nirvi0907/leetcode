class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, cols
        top, bottom = 0, rows
        spiral_order = []
        while left<right:
            for idx in range(left, right):
                spiral_order.append(matrix[top][idx])

            top+=1
            if top>=bottom:
                break
            for idx in range(top, bottom):
                spiral_order.append(matrix[idx][right-1])
            
            right-=1
            if left>=right:
                break
            for idx in range(right-1, left-1, -1):
                spiral_order.append(matrix[bottom-1][idx])
            bottom-=1
            if top>=bottom:
                break
            for idx in range(bottom-1, top-1, -1):
                spiral_order.append(matrix[idx][left])
            
            left+=1

        return spiral_order

'''
make sure lef<right and top<bottom otherwise we will rpeeat numbers, so whenever we increase or decrease these vars we check for left>=right or top>=bottom we break
'''
