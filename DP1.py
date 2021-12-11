##MLIS: maxLengthIncreasingSubSequence
# 1  5 2 4 3 -> 3
def maxLISS(nums):
    def L(nums, i):
        memo={}
        #base:
        if i in memo:
            return memo[i]
        if i==len(nums)-1:
            return 1
        max_len=1
        for j in range(i+1,len(nums)):
            if nums[j]>nums[i]:
                max_len=max(max_len,L(nums,j)+1)
        memo[i]=max_len
        return max_len
    return max( list(L(nums,i) for i in range(len(nums)))) 

def maxLISS2(nums):

    dp_arr=[1]*len(nums)
    for i in reversed(range(len(nums))):
        # 4,3,2,1,0
        for j in range(i+1,len(nums)):
            if nums[j]>nums[i]:
                dp_arr[i] =max(dp_arr[i],dp_arr[j]+1)
    return max(dp_arr)

res=maxLISS2([1,5,2,4,3])
print(res)