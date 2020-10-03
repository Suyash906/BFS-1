from collections import defaultdict
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1:return True
        
        indegree = [0 for _ in range(numCourses)]
        dependant_map = defaultdict(list)
        for c1, c2 in prerequisites:
            indegree[c2]+=1
            dependant_map[c1].append(c2)
        q = deque([])
        for i, val in enumerate(indegree):
            if val == 0:
                q.append(i)
                
        if len(q) == 0:return False
        
        count = 0
        
        while q:
            curr = q.popleft()
            count+=1
            for index in dependant_map[curr]:
                indegree[index]-=1
                if 0 == indegree[index]:
                    q.append(index)
        
        return count == numCourses