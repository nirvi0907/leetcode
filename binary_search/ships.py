'''
1011. Capacity To Ship Packages Within D Days
Solved
Medium
Topics
Companies
Hint

A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
'''

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        edge cases- days=0, weights=[], 
        ''' 
        def can_deliver(mid_weight):
            delivery_days = 1
            cursum=0
            for weight in weights:
                if weight>mid_weight:
                    return False
                cursum+=weight
                if cursum>mid_weight:
                    delivery_days+=1
                    cursum=weight
            return delivery_days<=days  

        low, high = min(weights), sum(weights)
        min_weight = 0
        while low<=high:
            mid = (low+high)//2
            if can_deliver(mid):
               min_weight = mid
               high = mid-1
            else:
                low = mid+1
        return min_weight
