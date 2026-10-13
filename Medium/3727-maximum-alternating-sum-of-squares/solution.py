class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Sort squares of elements to maximize positive terms and minimize negative terms
        squares = sorted(x * x for x in nums)
        k = (len(nums) + 1) // 2
        return sum(squares[-k:]) - sum(squares[:-k])