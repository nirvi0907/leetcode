class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        res = []
        #since we are moving from high to lower on both sides of 0 in number license()
        #we check for higher one out of left or right and move forward
        while l<=r:
            right_sqr = nums[r]*nums[r]
            left_sqr = nums[l]*nums[l]
            if right_sqr<left_sqr:
                res.append(left_sqr)
                l+=1
            elif right_sqr>=left_sqr:
                res.append(right_sqr)
                r-=1
            

        return res[::-1]
