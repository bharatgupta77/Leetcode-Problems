class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        while(i<len(nums)-2):
            if(nums[i] == nums[i+1]):
                i+=2
                continue
            else:
                return nums[i]
            
        return nums[-1]
                
 
        
            
        