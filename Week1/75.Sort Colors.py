#Two pointers
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left=0
        n=len(nums)
        while left<n-1:
            for right in range(left+1,n):
                if nums[right] < nums[left]:
                    temp=nums[left]
                    nums[left]=nums[right]
                    nums[right]=temp
            left+=1

#Simple one line solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums[:] = [0]*nums.count(0)+[1]*nums.count(1)+[2]*nums.count(2)
