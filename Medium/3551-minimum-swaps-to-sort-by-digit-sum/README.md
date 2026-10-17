# 3551. Minimum Swaps to Sort by Digit Sum

- **Difficulty:** Medium
- **Topics:** Array, Hash Table, Sorting
- **Solved:** 2026-10-17
- [View on LeetCode](https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 1206 ms (beats 46.9%) | 44.7 MB (beats 77.0%) |

## Notes

Approach: Compute digit sums, pair each element with its digit sum and original index, and sort to find the target permutation. Then, count the number of disjoint permutation cycles to compute the minimum swaps required as the sum of `(cycle_size - 1)`.
Time: O(N log N)
Space: O(N)
