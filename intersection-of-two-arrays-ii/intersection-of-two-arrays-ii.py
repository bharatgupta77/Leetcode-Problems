class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l = []
        for i in nums1:
            for j in nums2:
                if i == j :
                    l.append(i)
                    nums2.pop(nums2.index(j))
                    break
        return l
            
            
            
            
        