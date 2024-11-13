class Solution:
    def countFairPairs(self, v, lower, upper):
        v.sort()
        ans = 0
        print(v)
        for i in range(len(v) - 1):
            #we are asking lower<=v[idx]+X<=upper, how many X are there
            #example for 0 in input1, there 3 Xs, i.e 4,4,5
            #https://www.youtube.com/watch?v=htLqEd6tge4
            low = bisect_left(v, lower - v[i], i + 1)
            
            # print(low)
            up = bisect_right(v, upper - v[i], i + 1)
            print(" idx ", i, ":", low, ":", up)
            ans += up - low
        return ans