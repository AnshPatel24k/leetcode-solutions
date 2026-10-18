import math
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(arr: List[int]) -> int:
            # Base case: arrays with 2 or fewer elements have only 1 unique BST arrangement
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            # Combine the subtrees and account for interleaving arrangements
            total_ways = math.comb(len(left) + len(right), len(left))
            return (total_ways * dfs(left) * dfs(right)) % MOD
            
        # Subtract 1 to exclude the original array permutation itself
        return (dfs(nums) - 1) % MOD
