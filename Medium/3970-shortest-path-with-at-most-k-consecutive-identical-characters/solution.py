import heapq
from typing import List


# Dijkstra's algorithm over state (node, consecutive_identical_count)
class Solution:

    def shortestPath(
        self, n: int, edges: List[List[int]], labels: str, k: int
    ) -> int:
        if n == 1:
            return 0

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w, labels[u] == labels[v]))

        K1 = k + 1
        dist = [float("inf")] * (n * K1)

        # Start at node 0 with count 1
        dist[1] = 0
        pq = [(0, 0, 1)]  # (distance, node, count)

        while pq:
            d, u, count = heapq.heappop(pq)

            if u == n - 1:
                return d

            idx = u * K1 + count
            if d > dist[idx]:
                continue

            for v, w, same in adj[u]:
                next_count = count + 1 if same else 1
                if next_count <= k:
                    next_idx = v * K1 + next_count
                    if d + w < dist[next_idx]:
                        dist[next_idx] = d + w
                        heapq.heappush(pq, (d + w, v, next_count))

        return -1