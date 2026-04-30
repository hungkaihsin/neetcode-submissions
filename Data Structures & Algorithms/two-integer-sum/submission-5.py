class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_position = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_position:
                return [num_position[complement], i]
            num_position[nums[i]] = i
        
        