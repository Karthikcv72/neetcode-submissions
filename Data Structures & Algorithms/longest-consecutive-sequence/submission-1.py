class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=set(nums)
        mx=0
        for num in nums:
            if num-1 in arr:
                continue
            c=1
            while(num+c in arr):
                c+=1
            mx=max(mx,c)
        return mx