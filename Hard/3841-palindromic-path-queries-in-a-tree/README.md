# 3841. Palindromic Path Queries in a Tree

- **Difficulty:** Hard
- **Topics:** Array, String, Divide and Conquer, Bit Manipulation, Tree, Depth-First Search, Binary Indexed Tree, Segment Tree
- **Solved:** 2026-10-29
- [View on LeetCode](https://leetcode.com/problems/palindromic-path-queries-in-a-tree/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 2288 ms (beats 10.2%) | 121.1 MB (beats 16.3%) |

## Notes

Approach:
We represent each character set on a path using a 26-bit integer mask where the $k$-th bit indicates whether character $k$ appears an odd number of times. Using Euler tour order (DFS entry/exit times), updating a node's character corresponds to XOR-ing a value over the subtree's range $[in[u], out[u]]$, which is maintained using a Fenwick tree configured for range XOR updates and point queries. LCA is queried in $O(1)$ time using an Euler Tour Sparse Table, making each update and query run in $O(\log N)$ time.

Time: O((N + Q) \log N)
Space: O(N \log N)
