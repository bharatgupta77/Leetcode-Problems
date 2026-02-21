# Longest Consecutive Sequence

> 📅 Solved: 2026-02-21 | 🏷️ Difficulty: **medium** | 💻 Language: **Python3**
> ⏱️ Runtime: **51 ms** | 💾 Memory: **36.8 MB**

---

## 📝 Problem Description

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

	There is no string in strs that can be rearranged to form "bat".

	The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.

	The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

	1 <= strs.length <= 104

	0 <= strs[i].length <= 100

	strs[i] consists of lowercase English letters.

---

## ✅ My Solution

```python
                length = 1
                
                    current_num += 1
                    length += 1
                
                while current_num + 1 in s:
                max_length = max(max_length, length)

        return max_length


                current_num = num
            if (num-1) not in s:
        for num in s:


        length = 0
        max_length = 0

```

---

*Saved automatically on Accepted verdict via [LeetCode GitHub Saver](https://github.com)*
