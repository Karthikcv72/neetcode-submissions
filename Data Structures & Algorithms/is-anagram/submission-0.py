class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map1=Counter(s)
        map2=Counter(t)
        return map1==map2
