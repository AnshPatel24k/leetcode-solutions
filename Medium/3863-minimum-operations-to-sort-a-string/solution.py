from itertools import pairwise

class Solution:
    def minOperations(self, s: str) -> int:
        # Check if already sorted
        if all(a <= b for a, b in pairwise(s)):
            return 0
            
        if len(s) == 2:
            return -1
            
        mn, mx = min(s), max(s)
        
        # 1 Operation possible
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # 2 Operations possible if min or max exists in the middle
        if any(c in (mn, mx) for c in s[1:-1]):
            return 2
            
        # 3 Operations needed otherwise
        return 3
