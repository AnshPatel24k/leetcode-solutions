# 462. Minimum Moves to Equal Array Elements II

- **Difficulty:** Medium
- **Topics:** Array, Math, Sorting
- **Solved:** 2026-11-03
- [View on LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 2 ms (beats 88.7%) | 20.3 MB (beats 92.5%) |

## Notes

Approach: Sorting the array allows us to pair each element from the left with its corresponding element from the right. The minimum moves to make any pair equal is simply their difference, and summing these pairwise differences gives the minimum total moves (which implicitly uses the median as the target value).
Time: O(n log n)
Space: O(1)
