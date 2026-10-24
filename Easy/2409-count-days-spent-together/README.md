# 2409. Count Days Spent Together

- **Difficulty:** Easy
- **Topics:** Math, String
- **Solved:** 2026-10-24
- [View on LeetCode](https://leetcode.com/problems/count-days-spent-together/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 0 ms (beats 100.0%) | 19.4 MB (beats 47.3%) |

## Notes

Approach:
Convert each "MM-DD" date string to a 1-indexed day of the year using the month lengths of a non-leap year. The overlap between Alice's and Bob's stays is then the range between the maximum arrival day and the minimum departure day.

Time: O(1)
Space: O(1)
