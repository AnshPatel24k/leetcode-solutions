# 2089. Find Target Indices After Sorting Array

- **Difficulty:** Easy
- **Topics:** Array, Binary Search, Sorting
- **Solved:** 2026-10-19
- [View on LeetCode](https://leetcode.com/problems/find-target-indices-after-sorting-array/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 1 ms (beats 33.5%) | 19.3 MB (beats 24.2%) |

## Notes

Approach: Count the number of elements strictly smaller than target and the number of elements equal to target; the target indices in the sorted array will be a contiguous range starting from the count of smaller elements.
Time: O(N)
Space: O(1)
