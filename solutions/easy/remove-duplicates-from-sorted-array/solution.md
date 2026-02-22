# Remove Duplicates from Sorted Array

> 📅 Solved: 2026-02-22 | 🏷️ Difficulty: **easy** | 💻 Language: **Python3**
> ⏱️ Runtime: **4 ms** | 💾 Memory: **20.7 MB**

---

## 📝 Problem Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

	1 <= s.length <= 2 * 105

	s consists only of printable ASCII characters.

---

## ✅ My Solution

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = 0

        while j < len(nums):

            if nums[i] != nums[j]:
            else:
                j+=1
            
                nums[i+1] = nums[j]
                i+=1
        
        return i+1
                j+=1

```

---

*Saved automatically on Accepted verdict via [LeetCode GitHub Saver](https://github.com)*
