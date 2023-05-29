class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        su,num,flag = 1,0,0
        
        s = s.lstrip()
        
        if len(s) == 0: 
            return 0
        
        if s[0] == "-":
            su = -1
            
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
                flag = 1
            elif (i == "+" or i == "-") and (flag == 0):
                flag = 1
                pass
            else: break
                
        num = num*su
        if (-2**31<=num<=(2**31)-1): return num
        if num<0: return -2**31
        else: return 2**31-1
        
        if(sum > ((2)**(31))-1):
            return ((2)**(31))-1
        elif(sum < ((-2)**(31))):
            return (-2)**(31)
        else:
            return sum
            
        