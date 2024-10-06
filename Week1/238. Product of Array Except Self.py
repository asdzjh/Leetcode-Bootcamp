#Prefix and suffix, all clear
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n      
        prefix = 1
        for i in range(0,n):
            answer[i]*=prefix
            prefix*=nums[i]         
        suffix = 1
        for i in range(n-1,-1,-1):
            answer[i]*=suffix
            suffix*=nums[i]
        return answer
