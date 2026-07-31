# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

**Difficulty**: Easy

**Status**: Pending

---
## Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Consider the number of _unique elements_ in `nums` to be `k**​​​​​​​**`​​​​​​​. After removing duplicates, return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique numbers in **sorted order**. The remaining elements beyond index `k - 1` can be ignored.

**Custom Judge:**

The judge will test your solution with the following code:

```python
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

```

If all assertions pass, then your solution will be **accepted**.

--- 
**Example 1:**

**Input:** nums = [1,1,2]

**Output:** 2, nums = [1,2,_]

**Explanation:** Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.

It does not matter what you leave beyond the returned k (hence they are underscores).

---
**Example 2:**

**Input:** nums = [0,0,1,1,1,2,2,3,3,4]
**Output:** 5, nums = [0,1,2,3,4,_,_,_,_,_]
**Explanation:** Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

## Intuition

Because the input array is already sorted, every duplicate appears immediately after its first occurrence. Then, the criteria for discriminating duplicates can be reduced to whether the current number equals their last neighbor.

```Plaintext
nums = [1, 2, 2, 3, 4]
			  ↑
		(nums[2] == nums[1]) → Duplicate
		
```

My earliest attempts were to iterate over the array and delete a duplicate number once encountered, by using either `List.pop(index)` or `List.remove(value)`. But this approach modifies the list that is used as base for the iterator on every deletion, which shift every following index. Completing this approach would require iterating over a copy of the original array, which defeats the constraint of editing the lists in place of the exercise. 

Instead of deleting elements, we can overwrite duplicates with the next unique value. 

This approach uses two moving pointers: 
- **Read pointer ($i$)**: scans every element
- **Write pointer ($w$)**: marks where the next unique value should be written

Whenever the read pointer finds a value different from the previous one, that value belongs in the unique prefix of the array, so it is copied to the write position.

For example,

```Plaintext
# Iteration 1
	nums = [1, 2, 2, 3, 4]
i:          ^      
w:          ^
```

The first digit is never a duplicate so we copy this value in place and move both of our pointers. Notice that we're overriding the actual value from `nums[0]`, although the new value is equal to the original.

```Plaintext
# Iteration 2
	nums = [1, 2, 2, 3, 4]
i:             ^      
w:             ^
```

We've found a unique value (different from the previous one), so we copy the value and move our pointers.

```Plaintext
# Iteration 3
	nums = [1, 2, 2, 3, 4]
i:                ^      
w:                ^
```

This is a duplicate, so we won't write anything, position `nums[1]` keeps holding our last unique value. We'll move only our Read pointer.

```Plaintext
# Iteration 4
	nums = [1, 2, 2, 3, 4]
i:                   ^      
w:                ^
```

The number 3 is a unique value, so we'll copy its value into our Write pointer and advance both pointers. This is the first actual modification of our list, the value from our Read pointer at `nums[3]` is assigned to the position of our Write pointer at `nums[2]`. Then we advance both pointers. 

```Plaintext
# Iteration 5
	nums = [1, 2, 3, 3, 4]
i:                      ^      
w:                   ^
```

The number 4 is another unique value so we'll close the loop with the following results: 

```Python
nums = [1, 2, 3, 4, 4]
w = 4
```

Being `w = 4` immediately after our last unique value, we can safely discard the values after `nums[w]`.

## Algorithm 

```mermaid
graph TD

    START((removeDuplicates))

    input[/"Input: 
    **nums**: List[int]"/]

    init[Initialize read and write pointers]

    scan{Read pointer<br/>at end?}

    unique{Current value<br/>different from previous?}

    copy[Copy value to write position]

    moveRead[Advance read]

    moveBoth[Advance read<br/>and write]
	
	trim[trim values from write pointer]
    
    END([Return nums])

    START --> input --> init --> scan
    scan -- No --> unique
    unique -- Yes --> copy --> moveBoth --> scan
    unique -- No --> moveRead --> scan
    scan -- Yes --> trim --> END
```


## Implementation

A Python for loop saves us from manually managing the Read pointer. From there the implementation is fairly simple

```python
from typing import List


class Solution:
	def removeDuplicates(self, nums: List[int]) -> List[int]:
		if not nums:
			return []
		w = 1
		for i in range(1, len(nums)):
			if nums[i] != nums[i -1]:
				nums[w] = nums[i]
				w+=1
		return nums[:w]

```


## Takeaways

- **Mutation and Iteration Hazards:** Mutating a collection (via `pop()` or `remove()`) while iterating over its index or iterator shifts subsequent elements unpredictably. This invalidates remaining loop bounds or skips elements unless working on a copy.
    
- **In-Place Transformation via Two Pointers:** When memory constraints prohibit auxiliary data structures or copies, a read-write pointer pattern allows linear $O(n)$ time and $O(1)$ space restructuring by partitioning the array into processed (unique) and unprocessed regions.
    
- **Interface vs. Implementation Constraints:** Standard platform signatures often specify returning an integer length to validate in-place modifications without allocating a new slice. However, returning a sliced view (`nums[:w]`) satisfies functional requirements when API contracts demand returning the modified collection directly.