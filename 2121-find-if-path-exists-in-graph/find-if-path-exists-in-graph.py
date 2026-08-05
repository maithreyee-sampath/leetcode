class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict, deque
        graph = defaultdict(list)

        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        visited = set()
        visited.add(source)

        q = deque()
        q.append(source)

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        if destination in visited:
            return True
        else:
            return False
