class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged =[]
        merged = self.merge(nums1,nums2)
        length = len(merged)
        if length %2 ==0:
            return (merged[length//2] + merged[length//2 -1])/2
        else:
            return merged[length//2]
    
    
    def merge(self, nums1, nums2):
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        i,j =0,0
        merged=[]
        while i<len(nums1) and j <len(nums2):
            if i<len(nums1)-1 and nums1[i]< nums2[j]:
                merged.append(nums1[i])
                i+=1
            if j< len(nums2) and nums2[j]<nums1[i]:
                merged.append(nums2[j])
                j+=1
        if i <len(nums1):
            merged.append(nums1[i])
            i+=1
        if j<len(nums2):
            merged.append(nums2[j])
            j+=1
        return merged
            
                
        