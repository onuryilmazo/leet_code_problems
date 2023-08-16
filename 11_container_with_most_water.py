from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            area = (right - left) * min(height[left], height[right])
            '''
            if (area > max_area):
                area = max_area
                aşağıdaki kod çok daha okunaklı ve güzel
            '''
            max_area = max(max_area,area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

height = [1,1]
area = Solution()
result = area.maxArea(height)
print(result)