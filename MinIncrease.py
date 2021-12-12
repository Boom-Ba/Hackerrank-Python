
def maxFrequency(nums, k):
    res=0
    left=0
    for right in range(len(nums)):
        k+=nums[right]
        if k< nums[right]*(right-left+1):
            k-=nums[left]
            left+=1        
    return right-left+1

res=maxFrequency([3,6,9],2)
print(res)