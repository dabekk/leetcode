class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        for i in range(0, len(heights)):
            for j in range(len(heights) - 1, i + 1, -1):
                height = min(heights[i], heights[j])
                width = j - i
                volume = height * width
                if(volume > result):
                    result = volume
                
        # print("result: " + str(result))
        return result
        
