class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.lower()
        s2= ''.join(filter(str.isalnum, s1))
        '''isalnum() Method and filter() Function  is used to Remove All Non-Alphanumeric Characters in Python String'''
        if s2==s2[::-1]:
            return True
        else:
            return False
        
        