# Longest Substring Without Repeating Characters

> 📅 Solved: 2026-03-02 | 🏷️ Difficulty: **medium** | 💻 Language: **Python3**
> ⏱️ Runtime: **11 ms** | 💾 Memory: **19.2 MB**

---

## 📝 Problem Description

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

	0 <= s.length <= 5 * 104

	s consists of English letters, digits, symbols and spaces.

---

## ✅ My Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        longest_len = 0
        window = set()

        for right in range(0,len(s)):

            while s[right] in window:
                window.remove(s[left])
                left+=1

            
            window.add(s[right])

            curr_length = right - left + 1
            longest_len = max(longest_len, curr_length)

        
        return longest_len


        
```

---

*Saved automatically on Accepted verdict via [LeetCode GitHub Saver](https://github.com)*
