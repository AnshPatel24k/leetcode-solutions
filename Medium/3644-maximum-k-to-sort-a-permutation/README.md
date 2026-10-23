# 3644. Maximum K to Sort a Permutation

- **Difficulty:** Medium
- **Topics:** Array, Bit Manipulation
- **Solved:** 2026-10-23
- [View on LeetCode](https://leetcode.com/problems/maximum-k-to-sort-a-permutation/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 36 ms (beats 41.8%) | 32 MB (beats 45.1%) |

## Notes

Approach: Every misplaced element must participate in swaps, so $k$ must be a submask of all misplaced elements, making their bitwise AND $K$ the upper bound. Since $K \in [0, n-1]$ exists in the permutation and satisfies $x \text{ AND } K = K$ for all misplaced $x$, $K$ acts as a universal pivot to sort the array, making $K$ the maximum valid answer.
Time: O(n)
Space: O(1)
