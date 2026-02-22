# Valid Palindrome

> 📅 Solved: 2026-02-22 | 🏷️ Difficulty: **easy** | 💻 Language: **Python3**
> ⏱️ Runtime: **7 ms** | 💾 Memory: **19.7 MB**

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
        while l < r:

            if s[l].isalnum() == False:
                l+=1
            if s[r].isalnum() == False:
                r-=1
            if s[l].lower() == s[r].lower():
                
                continue
                continue
                l+=1

                r-=1
            else:
                return False
        r = len(s)-1
        l = 0


```

---

*Saved automatically on Accepted verdict via [LeetCode GitHub Saver](https://github.com)*
