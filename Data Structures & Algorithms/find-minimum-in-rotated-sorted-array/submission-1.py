class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: # mean we are in the left part
                l = m + 1 # set the pointer to the right
            else:
                r = m - 1 # set the pointer to the left
        
        return res

# O(logn) binary search
# O(1) constant