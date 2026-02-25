# Remove Nth Node From End of List

> 📅 Solved: 2026-02-25 | 🏷️ Difficulty: **medium** | 💻 Language: **Python3**
> ⏱️ Runtime: **0 ms** | 💾 Memory: **19.5 MB**

---

## 📝 Problem Description

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

 

Constraints:

	The number of nodes in the list is sz.

	1 <= sz <= 30

	0 <= Node.val <= 100

	1 <= n <= sz

 

Follow up: Could you do this in one pass?

---

## ✅ My Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        while n>0:
            fast = fast.next
            n-=1
        

        while fast.next:
            slow = slow.next
            fast = fast.next

        temp = slow.next
        slow.next = temp.next
        temp.next = None

        return dummy.next


        
        
```

---

*Saved automatically on Accepted verdict via [LeetCode GitHub Saver](https://github.com)*
