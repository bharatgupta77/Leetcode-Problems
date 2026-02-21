# Group Anagrams

> 📅 Solved: 2026-02-21 | 🏷️ Difficulty: **medium** | 💻 Language: **Python3**
> ⏱️ Runtime: **9 ms** | 💾 Memory: **22 MB**

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
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        for s in strs:
            key = ''.join(sorted(s))




            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        
        return list(groups.values())


```

---

*Saved automatically on Accepted verdict via [LeetCode GitHub Saver](https://github.com)*
