
class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        counter, pre_sum, res = collections.Counter(), 0, 0 
        counter[0] = 1
        for num in A:
            pre_sum += num 
            res += counter[pre_sum-S]
            counter[pre_sum] += 1
            
        return res 


        class Solution:
    def func(self, nums, goal):
        if goal < 0: return 0
        l = r = count = 0
        sum_ = 0

        for r in range(len(nums)):
            sum_ += nums[r]
            
            while sum_ > goal:
                sum_ -= nums[l]
                l += 1
            
            count += (r - l + 1)

        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        x = self.func(nums, goal)
        y = self.func(nums, goal - 1)
        return x - y

        https://www.youtube.com/watch?v=5Quv9nnZs34