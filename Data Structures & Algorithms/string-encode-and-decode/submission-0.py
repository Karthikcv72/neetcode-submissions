class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for i in strs:
            ans=ans+str(len(i))+'#'+i
        return  ans
    def decode(self, s: str) -> List[str]:
        ans=[]
        l=0
        while l<len(s):
            r=l
            while s[r]!='#':
                r+=1
            length=int(s[l:r])
            ans.append(s[r+1:r+length+1])
            l=r+length+1
        return ans