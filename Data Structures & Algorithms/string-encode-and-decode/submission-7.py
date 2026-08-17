class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for st in strs:
            s+=str(len(st))+'#'+st
        return s
    def decode(self, s: str) -> List[str]:
        ans=[]
        l=0
        while(l<len(s)):
            r=l
            while(s[r]!='#'):
                r+=1
            l=int(s[l:r])
            ans.append(s[r+1:r+l+1])
            l=r+l+1
        return ans