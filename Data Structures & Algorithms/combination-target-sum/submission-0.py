class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def backtracking(i,curr,total):
            if total==target:
                ans.append(curr[:])
                return
            if total>target or i>=len(nums):
                return
            curr.append(nums[i])
            backtracking(i,curr,total+nums[i])
            curr.pop()
            backtracking(i+1,curr,total)
        backtracking(0,[],0)
        return ans