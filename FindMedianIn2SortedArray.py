class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import statistics
        return statistics.median(sorted(nums1+nums2))
            
                
        