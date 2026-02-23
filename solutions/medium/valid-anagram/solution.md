# Valid Anagram

> 📅 Solved: 2026-02-23 | 🏷️ Difficulty: **medium** | 💻 Language: **Python3**
> ⏱️ Runtime: **15 ms** | 💾 Memory: **19.5 MB**

---

## 📝 Problem Description

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

 

Constraints:

	3 <= nums.length <= 3000

	-105 <= nums[i] <= 105

---

## ✅ My Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        result ={}

        for char in s:
            result[char] = result.get(char,0) + 1

        
        for char in t:
            if char not in result:
                return False
            result[char] -= 1
            if result[char] < 0:
                return False

        return True



        
```

---

*Saved automatically on Accepted verdict via [LeetCode GitHub Saver](https://github.com)*
