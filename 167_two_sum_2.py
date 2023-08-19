from typing import List
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,len(numbers)-1):
            for j in range(1,len(numbers)):
                if ((numbers[i] + numbers[j]) == target):
                    return[i+1, j+1]
        
        return []
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i, num in enumerate(numbers):
            complement = target - num

            if complement in num_to_index:
                return[num_to_index[complement]+1,i+1]

            num_to_index[num] = i
        return []


numbers = [1,2,3,5]
target = 8

answer = Solution()
result = answer.twoSum(numbers, target)
print(result)