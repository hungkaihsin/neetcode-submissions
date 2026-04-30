class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_position = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in number_position:
                return [number_position[complement], i]
            number_position[nums[i]] = i
        