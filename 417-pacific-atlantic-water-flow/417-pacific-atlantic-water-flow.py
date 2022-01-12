def getflow(heights, q, m, n):
    ans = set(q)
    while len(q):
        y,x = q.pop(0)
        ans.add((y,x))
        if(y, x+1) not in ans and x+1<n and heights[y][x+1]>=heights[y][x]:
            q.append((y,x+1))
        if(y, x-1) not in ans and x-1>-1 and heights[y][x-1]>=heights[y][x]:
            q.append((y,x-1))
        if(y-1, x) not in ans and y-1>-1 and heights[y-1][x]>=heights[y][x]:
            q.append((y-1,x))
        if(y+1, x) not in ans and y+1<m and heights[y+1][x]>=heights[y][x]:
            q.append((y+1,x))
    return ans
        
        
    
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        q = [(m-1,x) for x in range(n)]+[(x, n-1) for x in range(m-1)]
        atlantic = getflow(heights, q, m, n)
        q = [(0,x) for x in range(n)]+[(x,0) for x in range(1,m)]
        return atlantic.intersection(getflow(heights, q, m, n))
        
        
        