class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        []
        [1] [], [1]
        [1,2], [], [1], [2], [1,2]
        '''
        subsets = []
        def find_subsets(idx, subset):
            if idx == len(nums):
                subsets.append(subset.copy())
                return
            
            find_subsets(idx+1, subset+[nums[idx]])
            find_subsets(idx+1, subset)
        find_subsets(0, [])
        return subsets
        