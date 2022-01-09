class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        graph=[[0,set()] for x in range(n)]
        for d,s in pre:
            graph[s][1].add(d)
            graph[d][0]+=1
        q=[x for x in range(n) if graph[x][0]==0]
        ans=[]
        while q:
            node=q.pop(0)
            ans.append(node)
            for adjnode in graph[node][1]:
                if graph[adjnode][0]==1:
                    q.append(adjnode)
                else:
                    graph[adjnode][0]-=1
        return [] if len(ans)!=n else ans
        
        
        