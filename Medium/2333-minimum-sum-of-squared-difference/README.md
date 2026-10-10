# 2333. Minimum Sum of Squared Difference

- **Difficulty:** Medium
- **Topics:** Array, Binary Search, Greedy, Sorting, Heap (Priority Queue)
- **Solved:** 2026-10-10
- [View on LeetCode](https://leetcode.com/problems/minimum-sum-of-squared-difference/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 147 ms (beats 66.3%) | 36.4 MB (beats 97.5%) |

## Notes

Approach:
We compute the absolute differences between `nums1` and `nums2` and count their frequencies using a bucket array, since the maximum difference is at most $10^5$. We then greedily decrement the largest differences using our budget of $k = k1 + k2$ operations. Finally, we calculate the sum of the squared remaining differences.

Time: O(N + M) where N is the length of the arrays and M is the maximum possible difference (10^5).
Space: O(M) to store the frequencies of the differences.
