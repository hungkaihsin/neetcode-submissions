class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]

        for num, count in count_map.items():
            buckets[count].append(num)
        result = []
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result