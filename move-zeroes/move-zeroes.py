class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0;
        for i in range(0, len(nums)):
            if(nums[i] != 0 ):
                nums[count],nums[i] = nums[i],nums[count]
                count+=1                