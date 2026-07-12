class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False

# time O(n) time for iterate the input array
# space O(n) set