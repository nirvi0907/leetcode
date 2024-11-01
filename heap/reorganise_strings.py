class Solution:
    '''
    edge cases - what if freq of char is same then we have to get next diff char
    '''
    def reorganizeString(self, s: str) -> str:
        
        heap = []
        freqs = Counter(s)

        for char,freq in freqs.items():
            heapq.heappush(heap, (freq*-1, char))
        
        nonadjstr = ''
        while heap:
            if len(heap)==1 and (heap[0][0]*-1)>1:
                return ''
            freq, char = heapq.heappop(heap)
            if nonadjstr and nonadjstr[-1]==char:
               
                secondf, secondchar = heapq.heappop(heap)
                heapq.heappush(heap, (freq, char))
                freq, char = secondf, secondchar
             
            nonadjstr+=char
            freq = (freq*-1)-1
            if freq>0:
                heapq.heappush(heap, (freq*-1, char))
        return nonadjstr