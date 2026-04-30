class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count = {}
        for num in nums:
            number_count[num] = number_count.get(num, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]

        for num, count in number_count.items():
            buckets[count].append(num)
        result = []
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result