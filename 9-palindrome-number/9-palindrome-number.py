class Solution(object):
    def isPalindrome(self, x):
        res=str(x)
        if res==res[::-1]:
            return True
        return False
        
       
        