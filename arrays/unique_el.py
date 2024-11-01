
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #in this problem we need to convert nums in place, so that  all unique elements are in first k places
        # nums = [0,0,1,1,1,2,2,3,3,4]
        # shoudl be conevrted to nums = [0,1,2,3,4,_,_,_,_,_] all unqiie in first k places
        # for this we have 2 pointers, and we increment left only when we encounter unique elemnt at right(meanig cur not equal to prev)
        # last pos of left will benumber of unique elements
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left

      