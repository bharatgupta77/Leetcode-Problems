class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_dict:
                return [complement_dict[complement], i]
            complement_dict[num] = i




                    
