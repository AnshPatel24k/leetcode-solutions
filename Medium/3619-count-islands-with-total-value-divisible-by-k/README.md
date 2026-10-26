# 3619. Count Islands With Total Value Divisible by K

- **Difficulty:** Medium
- **Topics:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
- **Solved:** 2026-10-26
- [View on LeetCode](https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 265 ms (beats 91.4%) | 30 MB (beats 97.6%) |

## Notes

Approach:
We traverse the grid and use iterative Breadth-First Search (BFS) to explore each unvisited island (cells with value > 0). While exploring an island, we mark visited cells by setting their grid value to 0 and sum up all cell values in the island, then check if the total sum is divisible by $k$.

Time: O(m * n)
Space: O(m * n)
