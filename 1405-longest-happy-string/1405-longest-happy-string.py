class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans,c=[],{'a':a,'b':b,'c':c}
        while any(c.values()):#works until all values are vanished
            candidates=['a','b','c']
            if len(ans)>=2 and ans[-1]==ans[-2]:
                candidates.remove(ans[-1])
            max_char=max(candidates,key=lambda x:c[x])
            if not c[max_char]:
                break
            ans.append(max_char)
            c[max_char]-=1
        return ''.join(ans)
            
        