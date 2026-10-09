# 15. 3Sum

- **Difficulty:** Medium
- **Topics:** Array, Two Pointers, Sorting
- **Solved:** 2026-10-09
- [View on LeetCode](https://leetcode.com/problems/3sum/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 493 ms (beats 87.3%) | 22.3 MB (beats 55.8%) |

## Notes

Approach: Sort the array and use a three-pointer technique. Iterate through the array with a fixed element, and use a two-pointer approach for the remaining elements to find pairs that sum to the target. Skip duplicates to ensure the triplets are unique, and break early when the fixed element is positive.
Time: O(n^2)
Space: O(n) for the sorting overhead in Python (Timsort) or O(1) if sorting in-place without auxiliary space.
