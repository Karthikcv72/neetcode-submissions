class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=list(set(nums))
        if len(l)==len(nums):
            return False
        return True