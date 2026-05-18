class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]: # mean the target would be on the right
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]: # mean the target would be on the left
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
# time O(logn) binary search
# spae O(1) constant
            