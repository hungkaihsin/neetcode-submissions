class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {} # val: index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in preMap:
                return [preMap[diff], i]
            preMap[num] = i
    
# time O(n) interate the input array
# space O(n) hashmap