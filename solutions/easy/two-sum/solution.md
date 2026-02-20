# Two Sum

> 📅 Solved: 2026-02-20 | 🏷️ Difficulty: **easy** | 💻 Language: **Python3**
> ⏱️ Runtime: **0 ms** | 💾 Memory: **20.5 MB**

---

## 📝 Problem Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

	2 <= nums.length <= 104

	-109 <= nums[i] <= 109

	-109 <= target <= 109

	Only one valid answer exists.

 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

---

## ✅ My Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i,char in enumerate(nums):
            complement = target - char
            if complement in seen:
                return [seen[complement],i]
            
            seen[char] = i
        

```

---

*Saved automatically on Accepted verdict via [LeetCode GitHub Saver](https://github.com)*
