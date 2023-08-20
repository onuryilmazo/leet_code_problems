from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        deneme = []
        for i in range(len(nums) - 1, len(nums)-k-1, -1):
            deneme.append(nums[i])
            nums.remove(nums[i])
        for i in range(len(deneme)):
            nums.insert(0, deneme[i])
        return nums

class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        while(k!=0):
            i = len(nums) -1
            x = nums[i]
            nums.remove(x)
            nums.insert(0, x)
            k-=1   
        return nums

nums = [1,2,3,4,5,6,7] 
k = 3
solution = Solution()
result = solution.rotate(nums, k)
print(result)

