class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count = 0
        for i in nums:
            no_digits = 0
            while(i>0):
                no_digits +=1
                i = i//10
            if no_digits % 2 == 0:
                count+=1
        return count

        
        