class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum = 0 
        
        flag = False
        
        if (x<0): 
            x = x*(-1)
            flag = True
            
        while x>0:
            sum = sum*10 + (x%10)
            x=x/10
            
        if(flag == True):
            sum = sum * (-1)
            
        if (sum > (2**31)-1 or sum < -(2**31)):
            return 0
        
        return sum
        
            
            
            
        