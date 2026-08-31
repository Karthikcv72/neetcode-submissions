class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for idx,num in enumerate(nums):
            
            l=idx+1
            r=len(nums)-1
            if idx>0 and nums[idx]==nums[idx-1]:
                continue
            while(l<r):
                t=nums[l]+nums[r]+num
                if t==0:
                    ans.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    while nums[r]==nums[r+1] and l<r:
                        r-=1
                elif t>0:
                    r-=1
                else:
                    l+=1
        return ans
                