class Solution:
    def mySqrt(self, x: int) -> int:
        # Base cases: 0 and 1 are their own square roots
        if x < 2:
            return x
            
        left, right = 1, x // 2
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if mid * mid is less than or equal to x
            if mid * mid <= x:
                ans = mid        # Store the closest integer found so far
                left = mid + 1   # Try to find a larger value
            else:
                right = mid - 1  # mid * mid is too large, look lower
                
        return ans
