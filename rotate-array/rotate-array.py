class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n  # Effective number of rotations
        
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Reverse the entire array
        reverse(nums, 0, n-1)

        # Reverse the first k elements
        reverse(nums, 0, k-1)

        # Reverse the remaining elements
        reverse(nums, k, n-1)

        