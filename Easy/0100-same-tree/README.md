# 100. Same Tree

- **Difficulty:** Easy
- **Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree
- **Solved:** 2026-10-08
- [View on LeetCode](https://leetcode.com/problems/same-tree/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 0 ms (beats 100.0%) | 19.2 MB (beats 95.0%) |

## Notes

Approach:
The problem is solved using a recursive depth-first traversal. We check if both nodes are null (equal), if only one of them is null (not equal), and if their values differ (not equal). If none of these conditions are met, we recursively check if their left and right subtrees are identical.

Time: O(N) where N is the number of nodes in the smaller tree, as we visit each node at most once.
Space: O(H) where H is the height of the tree, representing the maximum call stack depth (O(N) in the worst case of a completely unbalanced tree).
