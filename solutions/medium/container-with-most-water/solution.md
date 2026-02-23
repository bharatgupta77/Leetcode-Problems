# Container With Most Water

> 📅 Solved: 2026-02-23 | 🏷️ Difficulty: **medium** | 💻 Language: **Python3**
> ⏱️ Runtime: **8 ms** | 💾 Memory: **29.9 MB**

---

## 📝 Problem Description

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

 

Constraints:

	n == height.length

	2 <= n <= 105

	0 <= height[i] <= 104

---

## ✅ My Solution

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_area = 0

        maxHeight = max(height) 

        while left < right:
            width = right-left
            area = (min(height[left], height[right])) * width
            max_area = max(max_area, area)

            if max_area >= maxHeight * (right - left):
                return max_area
            
            elif height[left] < height[right]:
                left+=1
            else:
                right-=1

        return max_area
            

            




        
```

---

*Saved automatically on Accepted verdict via [LeetCode GitHub Saver](https://github.com)*
