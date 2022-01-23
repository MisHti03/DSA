class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adjList=[[] for i in range(n)]
        
        for v,e in edges:
            adjList[v].append(e)
            adjList[e].append(v)
            
        queue=[start]
        visited=set([start])
        while queue:
            curr=queue.pop()
            if curr==end:
                return True
            for i in adjList[curr]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return False
        
        
        
        