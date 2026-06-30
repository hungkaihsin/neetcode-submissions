class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Hashset = set()

        for num in nums:
            if num in Hashset:
                return True
            Hashset.add(num)
        return False

# time O(n) the time to go through the elements of the input array
# space O(n) the size of input array