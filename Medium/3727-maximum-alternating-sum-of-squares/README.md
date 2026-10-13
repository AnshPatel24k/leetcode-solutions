# 3727. Maximum Alternating Sum of Squares

- **Difficulty:** Medium
- **Topics:** Array, Greedy, Sorting
- **Solved:** 2026-10-13
- [View on LeetCode](https://leetcode.com/problems/maximum-alternating-sum-of-squares/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 135 ms (beats 97.3%) | 32.7 MB (beats 73.6%) |

## Notes

Approach:
To maximize the alternating sum of squares, we assign the $\lceil n / 2 \rceil$ largest squared values to positive (even-indexed) positions and the remaining $\lfloor n / 2 \rfloor$ smallest squared values to negative (odd-indexed) positions. We accomplish this by computing the square of each element, sorting them, and subtracting the sum of the smaller half from the sum of the larger half.

Time: O(n log n)
Space: O(n)
