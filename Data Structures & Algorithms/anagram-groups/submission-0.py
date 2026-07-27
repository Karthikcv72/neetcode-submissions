class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for str in strs:
            key="".join(sorted(str))
            if key in hashmap:
                hashmap[key].append(str)
            else:
                hashmap[key]=[str]
        return list(hashmap.values())
