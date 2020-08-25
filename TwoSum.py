class Solution(object):
    def twoSum(self, nums, target):
        if not nums:
            return [-1,-1]
        d ={}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]], i]
            else:
                d[nums[i]] = i