# 3Sum

> 📅 Solved: 2026-02-23 | 🏷️ Difficulty: **easy** | 💻 Language: **Python3**
> ⏱️ Runtime: **671 ms** | 💾 Memory: **22.5 MB**

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
                    
                    j += 1
                    k -= 1

                elif nums[j] + nums[k] < target:
                    j+=1
                
                        k -= 1
                    while j < k and nums[k] == nums[k-1]:
                        j += 1
                    while j < j and nums[j] == nums[j+1]:
                    
                    result.append([nums[i], nums[j], nums[k]])
                if current_sum == target:
        
                current_sum = nums[j] + nums[k]
                else:
                    k-=1

```

---

*Saved automatically on Accepted verdict via [LeetCode GitHub Saver](https://github.com)*
