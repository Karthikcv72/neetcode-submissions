class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=1
        ans=[1]*len(nums)
        for i in range(len(nums)):
            ans[i]=a
            a*=nums[i]
        s=1
        for j in range(len(nums)-1,-1,-1):
            ans[j]*=s
            s*=nums[j]
        return ans