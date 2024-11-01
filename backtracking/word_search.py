https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        []
        ['a','b']
        ''
        'abc'
        'a'
        '''
        def is_valid(dx, dy):
            if dx>=0 and dy>=0 and dx<rows and dy<cols:
                return True
            return False

        def is_present(r, c, idx):
            if idx==len(word):
                return True
            if not is_valid(r, c):
                return False
            if board[r][c]==word[idx]:
                old_val = board[r][c]
                board[r][c] = '*'
                for dr,dy in [[1,0], [0,1], [-1,0], [0,-1]]:
                    dx, dy = dr+r, dy+c
                    if is_present(dx, dy, idx+1):
                        return True
                board[r][c] = old_val
            return False

        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if is_present(row, col, 0):
                    return True
        return False