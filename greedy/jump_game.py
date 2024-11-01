class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        # since its max, it means ex-- if jump is 5, it can jump 1,2,3,4,5, which means if any of these are already reachable from goal
        # hence one we know something reaches goal, we change the goal to cur idx
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i]>=goal:
                goal=i
        return True if goal==0 else False