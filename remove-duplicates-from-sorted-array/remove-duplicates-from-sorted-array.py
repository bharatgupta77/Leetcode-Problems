class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0;
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i+=1;
                nums[i] = nums[j]
        
        return i+1
                       
        
        
        
        
        
        
        # i=0
        # placeholder  = 0
        # l = len(nums)
        # while(i<l):
        #     placeholder = nums[i]
        #     if(placeholder == nums[i-1]):
        #         l=l-1
        #         nums.remove(placeholder)
        #     else:
        #         i+=1
        # return l 
            
        