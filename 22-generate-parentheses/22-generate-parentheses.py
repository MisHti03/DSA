class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        def backtrack(s,oc,cc):
            #open bracket count should be less than n and closed bracket count should be less than open bracket count
            if oc==cc==n:
                res.append(s)
                return
            if oc<n:
                backtrack(s+"(",oc+1,cc)
            if cc<oc:
                backtrack(s+")",oc,cc+1)
        backtrack("",0,0,)
        return res
    
        
        