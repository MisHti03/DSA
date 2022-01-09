class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        graph=[[0,set()] for x in range(n)]#indegree is 0 at start,outdegree
        for d,s in pre:
            graph[s][1].add(d)
            graph[d][0]+=1
        q=[x for x in range(n) if graph[x][0]==0]
        count=n
        while q:
            node=q.pop(0)
            count-=1
            for adjnode in graph[node][1]:
                if graph[adjnode][0]==1:
                    q.append(adjnode)
                else:
                    graph[adjnode][0]-=1
        return count==0
        
        
        