# 3882. Minimum XOR Path in a Grid

- **Difficulty:** Medium
- **Topics:** Array, Dynamic Programming, Bit Manipulation, Matrix
- **Solved:** 2026-10-28
- [View on LeetCode](https://leetcode.com/problems/minimum-xor-path-in-a-grid/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 719 ms (beats 90.8%) | 25.7 MB (beats 90.0%) |

## Notes

Approach: We maintain a row of sets representing all reachable XOR values at each column. For cell (i, j), we combine XOR states from the cell above and to the left, and XOR each value with grid[i][j]. Finally, we return the minimum value in the bottom-right cell's set.
Time: O(m * n * MAX_VAL), where MAX_VAL <= 1024.
Space: O(n * MAX_VAL) for storing sets of reachable XOR sums for the dynamic programming state.
