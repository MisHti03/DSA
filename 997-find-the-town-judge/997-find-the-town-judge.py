class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tlist=[[0,0] for x in range(n+1)]
        for t in trust:
            tlist [t[0]][1]+=1
            tlist [t[1]][0]+=1
        for i in range(1,n+1):
            if tlist[i][0]==n-1 and tlist[i][1]==0:
                return i 
        return -1
        