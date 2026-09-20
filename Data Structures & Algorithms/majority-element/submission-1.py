class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashset=set(nums)
        for num in hashset:
            if nums.count(num)>len(nums)//2:
                return num
        
