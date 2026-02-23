# 3Sum

> 📅 Solved: 2026-02-23 | 🏷️ Difficulty: **medium** | 💻 Language: **Python3**
> ⏱️ Runtime: **691 ms** | 💾 Memory: **22.2 MB**

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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(0,len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j  = i+1
            k = len(nums) - 1
            target = -nums[i]

            while j<k:
                current_sum = nums[j] + nums[k]
        
                if current_sum == target:
                    result.append([nums[i], nums[j], nums[k]])
                    
                    while j < j and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1

                elif nums[j] + nums[k] < target:
                    j+=1
                
                else:
                    k-=1
        
        return result

                


        
```

---

*Saved automatically on Accepted verdict via [LeetCode GitHub Saver](https://github.com)*
