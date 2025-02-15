class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        '''
        12219
        
        '''
        stack = []
        nums = list(nums)
        '''
        idea is we want to remove first higher digits we list in decreasing order
        and remove last high digits if increasing order
        '''
        for num in nums:
            while stack and stack[-1]>num and k>0:
                stack.pop()
                k-=1
            stack.append(num)
        #lets say k is still left (we still haev elements to remove)
        while stack and k>0:
            stack.pop()
            k-=1
        #moving first index to non zero element  
        first_index=0
        while stack and first_index<len(stack) and stack[first_index]=='0' :
            first_index+=1
        if  first_index==len(stack):
            return '0'
        return ''.join(stack[first_index:])

