# Two Sum

> 📅 Solved: 2026-02-20 | 🏷️ Difficulty: **unknown** | 💻 Language: **python3**
> ⏱️ Runtime: **0 ms** | 💾 Memory: **20.6 MB**

---

## 📝 Problem Description

Description not available.

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
