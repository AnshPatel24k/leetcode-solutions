

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count_less = sum(1 for x in nums if x < target)
        count_equal = sum(1 for x in nums if x == target)
        return list(range(count_less, count_less + count_equal))