from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        n, m = len(heights), len(heights[0]) #num of rows and cols
        pacific_q = deque()
        atlantic_q = deque()

        # right, left, bottom, up
        traversal = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for i in range(n):
            pacific_q.append((i, 0))
            atlantic_q.append((i, m-1))
        for j in range(m):
            pacific_q.append((0, j))
            atlantic_q.append((n-1, j))

        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                reachable.add((row, col))
                for x, y in traversal:
                    nr, nc = row+x, col+y
                    if nr < 0 or nr>= n or nc < 0 or nc >= m:
                        continue
                    if (nr, nc) in reachable:
                        continue
                    if heights[nr][nc] < heights[row][col]:
                        continue
                    queue.append((nr, nc))
            return reachable

            return
        
        p_reachable = bfs(pacific_q)
        a_reachable = bfs(atlantic_q)

        return list(p_reachable.intersection(a_reachable))