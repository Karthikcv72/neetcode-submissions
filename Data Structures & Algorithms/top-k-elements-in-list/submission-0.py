class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=Counter(nums)
        print(x.items())
        res=[]
        freq=[[] for i in range(len(nums)+1)]
        for val,fre in x.items():
            freq[fre].append(val)
        for i in range(len(freq)-1,0,-1):
            res.extend(freq[i])
            if len(res)==k:
                return res