class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        freq = [0] * 100001
        max_diff = 0
        for n1, n2 in zip(nums1, nums2):
            d = abs(n1 - n2)
            freq[d] += 1
            if d > max_diff:
                max_diff = d
                
        if max_diff == 0:
            return 0
            
        k = k1 + k2
        for v in range(max_diff, 0, -1):
            if freq[v] > 0:
                if k >= freq[v]:
                    k -= freq[v]
                    freq[v-1] += freq[v]
                    freq[v] = 0
                else:
                    freq[v-1] += k
                    freq[v] -= k
                    break
                    
        return sum(v * v * freq[v] for v in range(1, max_diff + 1))