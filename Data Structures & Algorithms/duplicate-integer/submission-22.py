class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False

# time O(n) time loop the array
# space O(n) the size of input array