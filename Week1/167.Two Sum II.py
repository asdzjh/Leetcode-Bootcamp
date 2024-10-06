#Brute force, pass 20/24, time limit exceed
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            second = target - numbers[i]
            for j in range(i+1,len(numbers)):
                if numbers[j] == second:
                    res.append(i+1)
                    res.append(j+1)
        return res
#Two pointers, all clear
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        n = len(numbers)
        left = 0
        right = n - 1
        while (right > left):
            if numbers[left] + numbers[right] < target:
                left+=1
            elif numbers[left] + numbers[right] > target:
                right-=1
            else:
                return [left+1,right+1]
        return res
