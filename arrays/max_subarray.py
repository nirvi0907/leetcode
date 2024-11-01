class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # TC-nlogn
        # sC-log n
        def maxSubArray(nums):
            if len(nums) == 1:
                return nums[0]
            
            mid = len(nums) // 2
            left_max = maxSubArray(nums[:mid])
            right_max = maxSubArray(nums[mid:])
            
            # Find the maximum sum subarray that crosses the middle element
            left_sum = float('-inf')
            sum = 0
            for i in range(mid-1, -1, -1):
                sum += nums[i]
                left_sum = max(left_sum, sum)
            right_sum = float('-inf')
            sum = 0
            for i in range(mid, len(nums)):
                sum += nums[i]
                right_sum = max(right_sum, sum)
            cross_max = left_sum + right_sum
            
            return max(left_max, right_max, cross_max)
        
        return maxSubArray(nums)