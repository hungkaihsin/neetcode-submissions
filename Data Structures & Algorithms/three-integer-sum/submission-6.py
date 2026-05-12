class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break # impossibe to get the answer
            if i > 0 and a == nums[i - 1]:
                continue # skip the same number
            l, r = i + 1, len(nums) - 1 # skip the first added number (a)
            
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 # skip if the next nums[l] has same number
        return res 

# time O(n ** 2)
# space O(1) constant input
