class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        dp=set()
        dp.add(0)
        target=sum(nums)//2
        for i in reversed(range(len(nums))):
            nextDp=set()
            for num in dp:
                if num==target:
                    return True
                nextDp.add(nums[i]+num)
                nextDp.add(num)
            dp=nextDp
        return True if target in dp else False
            