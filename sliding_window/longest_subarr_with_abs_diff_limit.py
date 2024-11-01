class Solution:
    def longestSubarray(self, nums, limit):
        #maintain 2 queues, min and max for cur window, we keep updating, these, 
        #both are monotnic queues
        #then if limit is reached, we pop from min and /or max if cur element is equal to first element
        maxq = deque()
        minq = deque()
        n = len(nums)
        j = 0
        ans = 0
        for i in range(n):
            while maxq and nums[i] > maxq[-1]:
                maxq.pop()
            maxq.append(nums[i])
            while minq and nums[i] < minq[-1]:
                minq.pop()
            minq.append(nums[i])
            if maxq[0] - minq[0] > limit:
                if nums[j] == maxq[0]:
                    maxq.popleft()
                if nums[j] == minq[0]:
                    minq.popleft()
                j += 1
            ans = max(ans, i - j + 1)
        return ans

