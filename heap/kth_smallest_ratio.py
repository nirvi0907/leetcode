class Solution:

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)
        #push initial fractions onto heap
        for i in range(n-1):
            heapq.heappush(heap,(arr[i]/arr[n-1],i,n-1))
        #pop the smallest fraction k times
        while k:
            fraction, i,j =heapq.heappop(heap)
            k-=1
        #if its possible to decrement j, recalculate the fraction and push onto heap
            if j-1 >i:
                new_fraction = arr[i]/arr[j-1]
                heapq.heappush(heap, (new_fraction, i, j-1))
                # print(heap)
        return [arr[i], arr[j]]