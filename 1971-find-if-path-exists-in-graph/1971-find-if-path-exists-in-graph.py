class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adjList=[[] for i in range(n)]
        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
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
        
        
        
        