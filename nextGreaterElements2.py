class Solution:
    def nextGreaterElements2(self, nums: List[int]) -> List[int]:
        n =len(nums)
        stack=[]
        res= [-1]*n
        nums*=2 
        #circular extend array 121121
        for i, num in enumerate(nums):
            while stack and stack[-1][1]< num:
                idx,val =stack.pop()
                res[idx%n] =num            
            stack.append((i,num))
        return res
                
        