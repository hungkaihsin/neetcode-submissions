class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        HashSet = set()
        for num in nums:
            if num in HashSet:
                return True
            HashSet.add(num)
        return False

# time O(n) loop
# space O(n) set
        