class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        tcount=[0 for i in range(n)]
        for t in edges:
            tcount[t[1]]+=1
        ans=[]
        for k in range(n):
            if tcount[k]==0:
                ans.append(k)
        return ans
        