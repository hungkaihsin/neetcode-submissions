class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for cnt in s:
                count[ord(cnt)- ord('a')] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())

# time O(m * n) m = length of the array, n = average length of the array
# sapce O(m) the number of unique word
