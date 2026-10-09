# 1541. Minimum Insertions to Balance a Parentheses String

- **Difficulty:** Medium
- **Topics:** String, Stack, Greedy, Bracket Sequences
- **Solved:** 2026-09-30
- [View on LeetCode](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)

## Solutions

| Language | Runtime | Memory |
|---|---|---|
| [python3](solution.py) | 54 ms (beats 87.7%) | 19.8 MB (beats 59.3%) |

## Notes

An elegant greedy approach can be used to solve this problem. We can iterate through the string and keep track of two variables:
1. `insertions`: the number of characters we need to insert to balance the string.
2. `right_needed`: the number of right parentheses `)` we currently need to match the open parentheses `(` we have seen so far.

Since each `(` needs two `)` to balance:
- When we encounter a `(`, we need 2 more `)`. If our current `right_needed` is odd, it means there is a previous `(` that has only matched one `)`. Because we are now starting a new `(` group, we must immediately insert a `)` to complete the previous pair. Thus, we increment `insertions` by 1 and decrement `right_needed` by 1 before adding the 2 needed for the new `(`.
- When we encounter a `)`, we decrement `right_needed` by 1. If `right_needed` becomes `-1` (meaning we got a `)` but had no unmatched `(`), we must insert a `(` before it. A `(` provides 2 `)`. Since we already consumed one `)`, we now need 1 more `)`. So we increment `insertions` by 1 and set `right_needed` to 1.

At the end of the string, any remaining `right_needed` represents the unmatched `)` that we must insert to balance the remaining open parentheses.



Approach: We use a greedy approach with a single pass to count the required insertions and the number of right parentheses needed.
Time: O(N) where N is the length of the string.
Space: O(1) auxiliary space.
