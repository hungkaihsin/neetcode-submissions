class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        
        while left < right:
            # 3. Calculate the area for the current container
            # Width is the distance between pointers
            width = right - left
            # Height is limited by the shorter of the two lines
            height = min(heights[left], heights[right])
            current_area = width * height

            # Update the maximum area if this one is bigger
            max_area = max(max_area, current_area)

            # 4. The core logic: move the pointer of the shorter line
            if heights[left] < heights[right]:
                left += 1  # Move the left pointer inwards
            else:
                right -= 1 # Move the right pointer inwards

        return max_area