# 1254. Number of Closed Islands

- **Difficulty:** Medium
- **Topics:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
- **Solved:** 2026-10-25
- [View on LeetCode](https://leetcode.com/problems/number-of-closed-islands/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 14 ms (beats 79.7%) | 20 MB (beats 37.8%) |

## Notes

Approach: First, use DFS to sink (turn to 1) all land cells connected to the grid boundaries, as they cannot form closed islands. Then, iterate through the inner cells and perform DFS to count and sink each remaining isolated island of land.
Time: O(m * n)
Space: O(m * n)
