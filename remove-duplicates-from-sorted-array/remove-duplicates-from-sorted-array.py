class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        placeholder  = 0
        l = len(nums)
        while(i<l):
            placeholder = nums[i]
            if(placeholder == nums[i-1]):
                l=l-1
                nums.remove(placeholder)
            else:
                i+=1
        return l 
            
        