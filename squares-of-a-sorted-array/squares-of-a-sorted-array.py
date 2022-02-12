class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x = map(lambda x: x**2, nums)
        return sorted(x)
        