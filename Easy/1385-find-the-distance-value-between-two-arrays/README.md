# 1385. Find the Distance Value Between Two Arrays

- **Difficulty:** Easy
- **Topics:** Array, Two Pointers, Binary Search, Sorting
- **Solved:** 2026-11-05
- [View on LeetCode](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 4 ms (beats 92.2%) | 19 MB (beats 96.2%) |

## Notes

Approach:
Sort `arr2` and for each element `x` in `arr1`, use binary search to check if there exists any element in `arr2` within the range `[x - d, x + d]`. If no such element exists, `x` contributes to the distance value.

Time: O((M + N) log M), where N is the length of `arr1` and M is the length of `arr2`.
Space: O(M) or O(1) auxiliary space used for sorting `arr2`.
