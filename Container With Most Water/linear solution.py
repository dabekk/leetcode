class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left_pos = 0
        right_pos = len(heights) - 1
        for i in range(0, len(heights) - 1):
            area = min(heights[left_pos], heights[right_pos]) * (right_pos - left_pos)
            result = max(result, area)
            if(heights[left_pos] < heights[right_pos]):
                left_pos += 1
            else:
                right_pos -= 1
        return result
        
