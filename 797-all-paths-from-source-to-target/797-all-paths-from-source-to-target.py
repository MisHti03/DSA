def f(src,graph):
    if src==len(graph)-1:
        return [[len(graph)-1]]
    ans=[]
    for adjnode in graph[src]:
        adjans=f(adjnode,graph)
        ans+=[[src]+x for x in adjans]
    return ans
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return f(0,graph)
    