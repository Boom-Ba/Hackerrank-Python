class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1: return 0
        #find max jump from each step
        l , r =0, nums[0]
        jump =1
        while r<len(nums)-1:
            jump+=1 #will need another jump
            next_pos= max([i+nums[i] for i in range(l,r+1)])
            l,r =r, next_pos
        return jump
            
            
        
        
        