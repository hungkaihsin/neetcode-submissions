class Solution:
    
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        # Initialize pointers and variables
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        total_water = 0

        while left < right:
            # The shorter wall is the limiting factor for water level
            if height[left] < height[right]:
                # Process from the left side
                if height[left] >= max_left:
                    # This bar is a new, taller left wall. It can't trap water.
                    max_left = height[left]
                else:
                    # This bar is shorter than the max_left wall. It can trap water.
                    total_water += max_left - height[left]
                left += 1
            else:
                # Process from the right side
                if height[right] >= max_right:
                    # This bar is a new, taller right wall.
                    max_right = height[right]
                else:
                    # This bar is shorter than the max_right wall.
                    total_water += max_right - height[right]
                right -= 1
        
        return total_water