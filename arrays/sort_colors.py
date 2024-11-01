class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        2,0,2,1,1,0
        """
        def swap(x,y):
            nums[x], nums[y]=nums[y], nums[x]
        l,r=0, len(nums)-1
        i=0
        while  i<=r:
            if nums[i]==2:
                swap(i, r)
                r-=1 
                # lets say we have - after swapping we got 0 in the i position, now we dont want to increment i in this case, because instead of incrementing, we would want to swap this with left next time, so 0 goes to left
                i-=1
            elif nums[i]==0:
                swap(i,l)
                l+=1
            i+=1
        return nums