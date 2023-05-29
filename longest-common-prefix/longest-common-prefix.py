class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """     
        if len(strs) == 0:
            return ""
    
        shortest_string = min(strs, key=len)
    
        for i, char in enumerate(shortest_string):
                for other in strs:
                    if other[i] != char:
                        return shortest_string[:i]
    
        return shortest_string
        