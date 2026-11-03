# Target value must be max(nums) since we can only increment elements.
# The total moves needed is sum(max(nums) - x for x in nums).

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        return sum(mx - x for x in nums)