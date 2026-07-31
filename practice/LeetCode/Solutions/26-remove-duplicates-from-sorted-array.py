from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        w = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[w] = nums[i]
                w+=1

        return nums[:w]

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
            ([1, 1, 2], [1, 2]),                                # Simple duplicates
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),  # Multiple duplicates
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),                 # No duplicates
            ([2, 2, 2, 2], [2]),                                # All duplicates
            ([], []),                                           # Empty list
            ([1], [1])                                          # Single element
        ]

    for i, (nums, expected) in enumerate(test_cases):
        result = sol.removeDuplicates(nums[:])
        if result == expected:
            print(f"Test {i+1} PASSED")
        else:
            print(f"Test {i+1} FAILED: Expected {expected}, got {result}")
