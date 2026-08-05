class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque

        m = len(image) #row
        n = len(image[0]) #col

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        org_color = image[sr][sc]
        q = deque()
        visited = set()
        q.append((sr,sc))
        visited.add((sr,sc))

        while q:
            r, c = q.popleft()
            image[r][c] = color

            for row, col in directions:
                nr, nc = r+row, c+col
                if (0 <= nr < m) and (0 <= nc < n) and image[nr][nc] == org_color and (nr, nc) not in visited:
                    q.append((nr, nc))
                    visited.add((nr, nc))

        
        return image