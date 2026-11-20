class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=Counter(nums)
        heap=[]
        for num in x.keys():
            heapq.heappush(heap,(x[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res    