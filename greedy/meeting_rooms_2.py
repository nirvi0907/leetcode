start_lst = [start for start,end in sorted(intervals)]
        end_lst = [end for start,end in sorted(intervals, key=lambda x:x[1])]
        # print(end_lst)
        start_idx, end_idx = 0, 0
        meetings = 0
        min_meetings = 0

        while end_idx<len(intervals) and start_idx<len(intervals):
            if start_lst[start_idx]>=end_lst[end_idx]:
                end_idx+=1
                meetings-=1
            else:
                meetings+=1
                start_idx+=1
            min_meetings = max(min_meetings, meetings)
        return min_meetings