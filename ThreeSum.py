class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        s= set()
        for i in range(len(nums)-2):
            s.clear()
            if i ==0 or nums[i]!=nums[i-1]:
                sum = 0- nums[i]
                low = i+1
                hi = len(nums)-1
                while low<hi:
                    if nums[low]+nums[hi] < sum:
                        low+=1
                    elif nums[low]+nums[hi] > sum:
                        hi-=1
                    else:
                        if nums[low] not in s:
                            s.add(nums[low])
                            res.append([nums[i],nums[low],nums[hi]])
                        else:
                            low+=1
                            hi-=1
        return res
                                        
                                        
                                        
        