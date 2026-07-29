# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

Status: Solved

Difficulty: Easy

## Problem Statement 

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return _the head of the merged linked list_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

**Input:** list1 = [1,2,4], list2 = [1,3,4]
**Output:** [1,1,2,3,4,4]

**Example 2:**

**Input:** list1 = [], list2 = []
**Output:** []

**Example 3:**

**Input:** list1 = [], list2 = [0]
**Output:** [0]

**Constraints:**

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.

---

## Intuition

Both lists are already sorted in non-decreasing order.
The key constraint is not to copy values in memory but to reuse the existing nodes from the input lists. That means we need to sequentially rewire each node up to the next sorted position. 

Our strategy will be compare the values at each firsts node, and assign the smallest to a dummy node. The dummy node simplifies handling the tail. As long as both lists have nodes left, we check which lists' value is the smaller. Once one of the lists has been exhausted, the unappended values from the other lists are appended and the resulting lists is returned.


```mermaid
graph TD
    START((Merge Two<br/>Sorted Lists))

    Input[/Input:<br/>list1, list2/]

    bound{Are both lists<br/>non-empty?}

    compare{Which front node<br/>is smaller?}

    append[Append smaller node<br/>to result]

    advanceList[Advance the list<br/>that supplied it]

    advanceTail[Advance result tail]

    leftovers[Append the remaining list]

    END([Return merged list])

    START --> Input --> bound
    bound -- Yes --> compare
    compare --> append --> advanceList --> advanceTail --> bound
    bound -- No --> leftovers --> END
		
```
### Implementation

1. Create a dummy node and a current pointer
2. While both lists have nodes:
	* compare the current values
	* attatch the smaller node to current.next 
	* advance the pointer of the list we took the node from
	* move current forward
3. When once lists is empty, attatch the rest of the other list
4. Return dummy.next (the real head of the merged list)

```python

from typing import Optional, Any
# Definition for singly-linked list (expanded).
class ListNode:
    def __init__(self, val: Any = 0, next=None):
        if next is not None and not isinstance(next, ListNode):
            raise TypeError("`next` must be a linked list or None")
        self.val = val
        self.next = next
        
    def __repr__(self) -> str:
        next_id = hex(id(self.next)) if self.next else None
        return f"ListNode(id={hex(id(self))}, val={self.val}: {type(self.val)}, next={next_id})"

    def inspect(self):
        current = self
        while current:
            print(current)
            current = current.next
        

class Solution: 
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        return result.next



```