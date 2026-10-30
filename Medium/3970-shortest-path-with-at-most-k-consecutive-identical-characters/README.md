# 3970. Shortest Path With At Most K Consecutive Identical Characters

- **Difficulty:** Medium
- **Topics:** String, Graph Theory, Heap (Priority Queue), Shortest Path
- **Solved:** 2026-10-30
- [View on LeetCode](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 280 ms (beats 77.1%) | 63.8 MB (beats 57.2%) |

## Notes

Approach:
We run Dijkstra's algorithm where each state is defined as `(node, count)`, representing the current node and the number of consecutive identical characters ending at that node. Moving from node `u` to node `v` increases `count` by 1 if `labels[u] == labels[v]`, or resets `count` to 1 if they differ, valid as long as `count <= k`.

Time: O(k * (V + E) * log(k * V))
Space: O(k * V + E)
