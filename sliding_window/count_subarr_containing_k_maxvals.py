class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        counter = 0
        max_val = max(nums)
        res = 0
        #we need to find min subarray containing k maxvals and then add to res
        for right in range(len(nums)):
            if nums[right]==max_val:
                counter+=1
            while counter>=k:
                if nums[left]==max_val:
                    counter-=1
                #we will increase left when we find  subarray containing k maxvals
                #and then adjust left so that we find min subarray that contains k maxvals

                left+=1
            #last val of left would have previous element as maxval, so we know adding current left would get num of subarrays
            res+=left
        return res
            

                