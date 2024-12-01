class Solution:

    def largestCombination(self, candidates: List[int]) -> int:
        longest_combo = 0
        '''
        at every pos from 0 - 32, we find candidates that are having & > 1
        '''
        for num in range(32):
            cursum = 0
            for candidate in candidates:
                if candidate & (2**num):
                    cursum+=1
            longest_combo = max(longest_combo, cursum)
        return longest_combo