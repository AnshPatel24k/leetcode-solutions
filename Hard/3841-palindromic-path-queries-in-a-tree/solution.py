import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)


class Solution:

    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        # Path query condition: string can be rearranged into a palindrome iff
        # at most one character appears an odd number of times (i.e. path_mask & (path_mask - 1) == 0).
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        in_time = [0] * n
        out_time = [0] * n
        first_occ = [-1] * n
        eul = []
        depth = []
        timer = 0

        def dfs(u, p, d):
            nonlocal timer
            timer += 1
            in_time[u] = timer
            first_occ[u] = len(eul)
            eul.append(u)
            depth.append(d)

            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1)
                    eul.append(u)
                    depth.append(d)

            out_time[u] = timer

        dfs(0, -1, 0)

        # Build Sparse Table for O(1) LCA queries
        M = len(eul)
        LOG = M.bit_length()
        st = [[0] * M for _ in range(LOG)]
        st[0] = list(range(M))

        for k in range(1, LOG):
            half = 1 << (k - 1)
            for i in range(M - (1 << k) + 1):
                idx1 = st[k - 1][i]
                idx2 = st[k - 1][i + half]
                st[k][i] = idx1 if depth[idx1] < depth[idx2] else idx2

        def get_lca(u, v):
            p1, p2 = first_occ[u], first_occ[v]
            if p1 > p2:
                p1, p2 = p2, p1
            k = (p2 - p1 + 1).bit_length() - 1
            idx1 = st[k][p1]
            idx2 = st[k][p2 - (1 << k) + 1]
            return eul[idx1] if depth[idx1] < depth[idx2] else eul[idx2]

        # Fenwick Tree for Range Update Point Query on Euler Tour
        bit = [0] * (n + 2)

        def bit_add(idx, val):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)

        def bit_query(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        val = [1 << (ord(c) - 97) for c in s]
        for u in range(n):
            bit_add(in_time[u], val[u])
            bit_add(out_time[u] + 1, val[u])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_val = 1 << (ord(parts[2]) - 97)
                diff = val[u] ^ new_val
                if diff:
                    val[u] = new_val
                    bit_add(in_time[u], diff)
                    bit_add(out_time[u] + 1, diff)
            else:
                u, v = int(parts[1]), int(parts[2])
                lca = get_lca(u, v)
                mask = bit_query(in_time[u]) ^ bit_query(in_time[v]) ^ val[lca]
                ans.append((mask & (mask - 1)) == 0)

        return ans