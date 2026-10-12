# 2897. Apply Operations on Array to Maximize Sum of Squares

- **Difficulty:** Hard
- **Topics:** Array, Hash Table, Greedy, Bit Manipulation
- **Solved:** 2026-10-12
- [View on LeetCode](https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 1231 ms (beats 87.2%) | 32.1 MB (beats 34.0%) |

## Notes

Approach: Bitwise operations allow shifting set bits across numbers to construct larger numbers. We count the frequency of set bits at each position and construct the $k$ largest possible numbers by greedily placing set bits into the top elements.
Time: O(N * B + K * B) where N is length of nums, K is given integer, and B = 30 is the number of bits.
Space: O(B) = O(1) auxiliary space to store bit counts.
