class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = {}
        for i in s:
            if (i in l.keys()):
                l[i]+=1
            else:
                l[i] = 1
        
        x = []
        for i,j in l.items():
            if(j == 1):
                x.append(s.index(i))
                
        if len(x) == 0:
            return -1
        
        return min(x)
            
                