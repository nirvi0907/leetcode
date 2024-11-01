class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # res = []
        
        # for i, item in enumerate(intervals):
        #     s = item[0]
        #     e = item[1]
        #     start = newInterval[0]
        #     end = newInterval[1]
        #     #if we have [1,5] as new interval, and curretn iten is [8, 12], then it means, whatever is after is greater and we can simply apprend to result
        #     if end<s:
        #         res.append(newInterval)
        #         res.extend(intervals[i:])
        #         return res
        #     #if we have new inteval as [1,5] and current item is [1,2], then we first add [1,2]
        #     elif start>e :
        #         res.append(item)
        #     # if we have overlpping interval
        #     else:
        #         newInterval=[min(start, s), max(end, e)]
        # res.append(newInterval)
                
        
        # return res
        # intervals = [[1,4],  [6,8]]
        # newInterval = [4,6]
        start, end = newInterval

        # All ends in intervals[:i] have end < newInterval[0]
        i = bisect_left(intervals, start, key=lambda pair: pair[1])
        # All starts in a[j:] have start > newInterval[1]
        j = bisect_right(intervals, end, key=lambda pair: pair[0])

        if i == j:
            intervals.insert(i, newInterval)
            return intervals
        print(i, j)
        min_start = min(intervals[i][0], start)
        max_end = max(end, intervals[j-1][1])
        merged_interval = [min_start, max_end]

        return intervals[:i] + [merged_interval] + intervals[j:]