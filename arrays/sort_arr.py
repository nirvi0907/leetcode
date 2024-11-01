class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(a, l1, l2):
            s=0
            l, r=0,0
            while l<len(l1) and r<len(l2):
                if l1[l]<l2[r]:
                    a[s]=l1[l]
                    l+=1
                    s+=1
                else:
                    a[s]=l2[r]
                    r+=1
                    s+=1
            while l<len(l1):
                a[s]=l1[l]
                l+=1
                s+=1
            while r<len(l2):
                a[s]=l2[r]
                r+=1
                s+=1                        
            return a

        def divide(li):
            if len(li)==1:
                return li
            mid = (len(li) // 2 )-1
            left = divide(li[:mid+1])
            right = divide(li[mid+1:])
            return merge(li, left, right)
        return divide(nums)