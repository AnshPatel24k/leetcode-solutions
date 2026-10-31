# 3963. Create Grid With Exactly One Path

- **Difficulty:** Easy
- **Solved:** 2026-10-31
- [View on LeetCode](https://leetcode.com/problems/create-grid-with-exactly-one-path/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 8 ms (beats 5.7%) | 19.2 MB (beats 49.8%) |

## Notes

Approach: Construct an L-shaped path of free cells along the first column and the bottom row, with all other cells set as obstacles to ensure exactly one path exists.
Time: O(m * n)
Space: O(m * n)
