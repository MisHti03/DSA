class Solution(object):
    def kthSmallest(self, matrix, k):
        l=matrix[0][0]
        r=matrix[-1][-1]
        while l<r:
            mid=l+(r-l)//2
            if sum(bisect.bisect(row,mid) for row in matrix)<k:
                l=mid+1
            else:
                r=mid
        return l
                
        
           