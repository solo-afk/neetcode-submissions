class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1 
        max = 0
        while left < right:
            curr = (right - left)*min(heights[left], heights[right])
            if curr > max:
                max = curr
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max