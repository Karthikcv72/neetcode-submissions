class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap=Counter(nums)
        for num,count in hashmap.items():
            if count>len(nums)//2:
                return num
        
