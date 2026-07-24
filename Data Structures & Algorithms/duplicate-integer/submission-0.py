class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x=Counter(nums)
        for i in x:
            if x[i] > 1:
                return True
        return False