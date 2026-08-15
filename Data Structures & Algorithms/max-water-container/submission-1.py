class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        left, right = 0, len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left

            res = max(res, (height*width))

            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
        
        return res