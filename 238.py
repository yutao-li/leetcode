from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        cur=nums[-1]
        for i in range(len(nums)-2,-1,-1):
          res[i]=cur
          cur*=nums[i]
        cur=nums[0]
        for i in range(1,len(nums)):
          res[i]*=cur
          cur*=nums[i]
        return res
      
res=Solution().productExceptSelf([1,2,3,4])
print(res)
