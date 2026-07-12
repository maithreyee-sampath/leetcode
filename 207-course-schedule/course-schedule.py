from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #example 2 has a cycle. so when you see a cycle: ret false

        graph = defaultdict(list) 
        indegree = [0 for _ in range(numCourses)]       
        for course in prerequisites:
            graph[course[1]].append(course[0])
            indegree[course[0]] +=1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        count_courses = 0
        while q:
            u = q.popleft()
            count_courses +=1

            for v in graph[u]:
                indegree[v] -=1
                if indegree[v] == 0:
                    q.append(v)
        return count_courses == numCourses


        
        