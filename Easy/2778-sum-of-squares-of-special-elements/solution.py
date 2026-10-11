class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        # Iterate through 1-indexed positions
        for i in range(1, n + 1):
            # Check if i divides n cleanly
            if n % i == 0:
                # Add the square of the element (convert back to 0-indexed)
                ans += nums[i - 1] ** 2
                
        return ans
