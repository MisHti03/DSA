class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l=title.split(" ")
        ans=[]
        for i in l:
            if (len(i)<3):
                ans.append(i.lower())
            else:
                ans.append(i.title())
        return " ".join(ans)
        
        