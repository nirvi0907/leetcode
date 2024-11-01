# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         seen = {0 : -1}
#         sum_residue = 0
#         for i, num in enumerate(nums):
#             sum_residue = (sum_residue + num) % k
#             if sum_residue in seen:
#                 if i - seen[sum_residue] >= 2:
#                     return True
#             else:
#                 seen[sum_residue] = i
#         return False 

        '''
s and x are prefix sum of contiguous array, and m is left out contiguous sum thats divible by k
        s-x = m
        (s-x)%k = m%k
        (s-x)%k = 0 (if m is divisible by k)

        s%k = x%k
        hence if we already have found a remianinder before we return true
        '''
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s, prev_d, set_d = 0, 0, set()
        for num in nums:
            s += num
            d = s%k
            if d in set_d:
                return True
            #because we want atleast 2 length "m"
            set_d.add(prev_d)
            prev_d = d
        return False 