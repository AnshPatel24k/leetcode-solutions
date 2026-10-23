# Approach: The minimum number of operations required is equal to the number of unique positive elements in nums.
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return len({x for x in nums if x > 0})