from typing import List
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        for i in range(1,len(nums)):
            if (nums[i] == nums[i-1]):
                k-=1
            else:
                nums
               
        return k
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j, nums
nums = [1,1,2] 
solution = Solution()
result = solution.removeDuplicates(nums)
print(result)
