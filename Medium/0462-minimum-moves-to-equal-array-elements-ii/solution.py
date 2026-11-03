class Solution:

    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[~i] - nums[i] for i in range(len(nums) // 2))