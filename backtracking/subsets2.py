class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        nums.sort()
        def dfs(i, c):
            if i>=l:
                res.append(c.copy())
                return
            
            c.append(nums[i])
            dfs(i+1, c)
            c.pop()
            #we dont want same numbers in same pos, so we move until we find next diff number
            while i+1<l and nums[i+1]==nums[i]: i+=1
            dfs(i+1, c)

        dfs(0, [])
        return res
