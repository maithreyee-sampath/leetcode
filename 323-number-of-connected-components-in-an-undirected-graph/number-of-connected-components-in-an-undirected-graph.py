class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for edge in edges:
            u = edge[0]
            v = edge[1]

            if u not in adj:
                adj[u] = []
            adj[u].append(v)
            if v not in adj:
                adj[v] = []
            adj[v].append(u)
        
        def dfsRec(adj,s,visited):
            visited[s]= True

            for v in adj[s]:
                if not visited[v]:
                    dfsRec(adj,v,visited)
        
        def dfs(adj,n):
            visited = [False]*n
            count = 0

            for u in range(n):
                if visited[u] == False:
                    count+=1
                    dfsRec(adj,u,visited)

            return count
        return dfs(adj,n)
