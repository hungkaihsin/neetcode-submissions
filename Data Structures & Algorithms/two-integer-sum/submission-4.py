class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashdict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashdict:
                return [hashdict[complement], i]
            hashdict[nums[i]] = i
