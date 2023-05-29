class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        shortest_string = min(strs, key=len)
    
        for i, char in enumerate(shortest_string):
                for other in strs:
                    if other[i] != char:
                        return shortest_string[:i]
    
        return shortest_string


# sol 2
#         if not strs:
#             return ""

#         prefix = strs[0]

#         for i in range(1, len(strs)):
#             while strs[i].find(prefix) != 0:
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""

#         return prefix

        