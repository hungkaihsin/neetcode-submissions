class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {} # value: index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in preMap:
                return [preMap[diff], i]
            preMap[num] = i

# time O(n) the time iterate the input array
# sapce O(n) hashmap
