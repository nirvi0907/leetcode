class Solution:

    def __init__(self, w: List[int]):
        self.cdf = [0]
        for weight in w:
            self.cdf.append(self.cdf[-1] + weight)
        print(self.cdf)
        # self.low = 0
        # self.high = len(self.w)-1
    
    def pickIndex(self) -> int:
        rand = random.randint(1, self.cdf[-1])
        idx = bisect.bisect_left(self.cdf, rand)
        return idx - 1
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
