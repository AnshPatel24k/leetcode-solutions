from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        if n < x * k:
            return -1
        
        # Phase 1: Compute window median costs in O(N log x) time
        left = SortedList()
        right = SortedList()
        left_sum = 0
        right_sum = 0
        
        # window_costs[i] stores the cost for the subarray nums[i : i + x]
        window_costs = [0] * (n - x + 1)
        
        for i in range(n):
            if not left or nums[i] <= left[-1]:
                left.add(nums[i])
                left_sum += nums[i]
            else:
                right.add(nums[i])
                right_sum += nums[i]
                
            if i >= x:
                out_val = nums[i - x]
                if out_val <= left[-1] and out_val in left:
                    left.remove(out_val)
                    left_sum -= out_val
                else:
                    right.remove(out_val)
                    right_sum -= out_val
            
            target_left_size = (min(i + 1, x) + 1) // 2
            
            while len(left) < target_left_size:
                val = right.pop(0)
                right_sum -= val
                left.add(val)
                left_sum += val
                
            while len(left) > target_left_size:
                val = left.pop(-1)
                left_sum -= val
                right.add(val)
                right_sum += val
                
            if i >= x - 1:
                median = left[-1]
                cost = (len(left) * median - left_sum) + (right_sum - len(right) * median)
                window_costs[i - x + 1] = cost

        # Phase 2: Iterative Space-Optimized Dynamic Programming
        # dp[i] represents the minimum operations starting from index i
        # Base case: 0 subarrays remaining requires 0 operations
        dp = [0] * (n + 1)
        
        for rem in range(1, k + 1):
            next_dp = [float('inf')] * (n + 1)
            
            # We traverse backward because each choice builds on subsequent indices
            for i in range(n - x, -1, -1):
                # Option 1: Skip the current index
                skip = next_dp[i + 1]
                
                # Option 2: Pick the subarray starting at index i
                take = window_costs[i] + dp[i + x]
                
                next_dp[i] = min(skip, take)
                
            dp = next_dp
            
        return dp[0] if dp[0] != float('inf') else -1
