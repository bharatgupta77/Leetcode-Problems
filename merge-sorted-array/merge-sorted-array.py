class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0,len(nums1)):
            if(i<m):
                continue
            else:
                nums1[i] = nums2[i-m-1]
        
        nums1.sort()
        return nums1
                
        
        
            