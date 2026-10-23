# Approach:
# Every misplaced element x (where nums[i] != i) must be moved, so any valid k must be a submask
# of x. Thus k must be a submask of the bitwise AND of all misplaced elements, K.
# Since nums is a permutation of 0..n-1, the value K is guaranteed to exist in nums. 
# For every misplaced element x, x AND K == K, which means K can act as a universal pivot to swap 
# any misplaced element into its correct position. Therefore, the maximum k is K (or 0 if already sorted).

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        for i, x in enumerate(nums):
            if x != i:
                ans = x if ans == -1 else ans & x
        return ans if ans != -1 else 0