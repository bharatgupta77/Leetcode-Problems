class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        needle_len = len(needle)
        haystack_len = len(haystack)
        
        for i in range(0,haystack_len):
            if(haystack[i: i + needle_len] == needle):
                return i
        
        return -1
                
        
        