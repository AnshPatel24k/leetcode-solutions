class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        
        tree_s1 = [0] * (4 * n)  
        tree_s2 = [0] * (4 * n)  
        lazy = [0] * (4 * n)     
        
        def push_down(node, l, r):
            if lazy[node] == 0:
                return
            val = lazy[node]
            lazy[node] = 0
            
            mid = (l + r) // 2
            left = 2 * node
            right = 2 * node + 1
            
            # Update left child
            len_l = mid - l + 1
            tree_s2[left] = (tree_s2[left] + 2 * val * tree_s1[left] + val * val * len_l) % MOD
            tree_s1[left] = (tree_s1[left] + val * len_l) % MOD
            lazy[left] += val
            
            # Update right child
            len_r = r - mid
            tree_s2[right] = (tree_s2[right] + 2 * val * tree_s1[right] + val * val * len_r) % MOD
            tree_s1[right] = (tree_s1[right] + val * len_r) % MOD
            lazy[right] += val

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                len_node = r - l + 1
                tree_s2[node] = (tree_s2[node] + 2 * val * tree_s1[node] + val * val * len_node) % MOD
                tree_s1[node] = (tree_s1[node] + val * len_node) % MOD
                lazy[node] += val
                return
            
            push_down(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, val)
            
            tree_s1[node] = (tree_s1[2 * node] + tree_s1[2 * node + 1]) % MOD
            tree_s2[node] = (tree_s2[2 * node] + tree_s2[2 * node + 1]) % MOD

        ans = 0
        last_seen = {}
        
        for r in range(n):
            x = nums[r]
            
            l = last_seen.get(x, -1) + 1
            
            
            update(1, 0, n - 1, l, r, 1)
            last_seen[x] = r
            
            ans = (ans + tree_s2[1]) % MOD
            
        return ans
