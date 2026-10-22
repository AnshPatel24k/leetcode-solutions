# 32. Longest Valid Parentheses

- **Difficulty:** Hard
- **Topics:** String, Dynamic Programming, Stack, Bracket Sequences
- **Solved:** 2026-10-22
- [View on LeetCode](https://leetcode.com/problems/longest-valid-parentheses/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 9 ms (beats 56.3%) | 20.4 MB (beats 62.4%) |

## Notes

Approach: Maintain a stack storing indices, initialized with -1 as a base. Push indices of '(' and pop for ')', updating the maximum length using the index remaining at the top of the stack, or pushing the current index if the stack becomes empty.
Time: O(n)
Space: O(n)
