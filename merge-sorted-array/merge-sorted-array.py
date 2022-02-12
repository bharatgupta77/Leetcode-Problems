class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = m-1
        y = n-1
        for i in range(len(nums1)-1, -1, -1):
            if y < 0 or (x >= 0 and nums1[x] > nums2[y]):
                nums1[i] = nums1[x]
                x -= 1
            else:
                nums1[i] = nums2[y]
                y -= 1
            
            
            
            
#         for i in range(0,len(nums1)):
#             if(i<m):
#                 continue
#             else:
#                 nums1[i] = nums2[i-m-1]
        
#         nums1.sort()
#         return nums1
        
            
            
                
                    
                    
                    
            
                
            

        
                
        
        
            