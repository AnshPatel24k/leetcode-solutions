class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 30
        
        for num in nums:
            for b in range(30):
                if (num >> b) & 1:
                    bit_counts[b] += 1
                    
        ans = 0
        for i in range(k):
            val = 0
            for b in range(30):
                if bit_counts[b] > i:
                    val |= (1 << b)
            ans = (ans + val * val) % MOD
            
        return ans