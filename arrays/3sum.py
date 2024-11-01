class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx in range(len(nums)-2):
            if idx!=0 and nums[idx]==nums[idx-1]:
                continue
            left, right = idx+1, len(nums)-1

            while left<right:

                if nums[idx]+nums[left]+nums[right]==0:
                    res.append([nums[idx], nums[left], nums[right]])
                    # 000
                    while nums[left]==nums[left+1] and (left+1)<right:
                        left+=1
                    left+=1
                elif (nums[idx]+nums[left]+nums[right])<0:
                    left+=1
                else:
                    right-=1
        return res

