class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height)-1
        leftMax, rightMax=height[0], height[len(height)-1]
        res=0
        while l<r:
            #as long as the other one is greater, the smaller one will always win
            #we know that the height on the right side will determine the amount of water trapped in the remaining positions between the pointers. Since rightMax is lower, it effectively "caps" the amount of water we can trap on that side.
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax, height[l])
                res+=leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax, height[r]) # notie here lets say rightmax is 1 and curretn height is 2, so 1-2 is negative, but whenever its negative it means we find new max, we can just take this current element as max and subtract by itself in next line
                res+=rightMax-height[r]
            print(
                "l ", l, "r ", r," res ", res
            )
        return res