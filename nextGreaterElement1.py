class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack =[]
        dic ={}
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                dic[stack[-1]] =nums2[i]
                stack.pop()
            stack.append(nums2[i])
        for ele in stack:
            dic[ele]=-1
        res= []
        for i in range(len(nums1)):
            res.append(dic[nums1[i]])
        return res
                
                
        