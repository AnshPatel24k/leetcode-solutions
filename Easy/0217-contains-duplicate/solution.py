# Approach: Convert the list into a hash set to remove duplicates, then compare the length of the set to the length of the original list.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
