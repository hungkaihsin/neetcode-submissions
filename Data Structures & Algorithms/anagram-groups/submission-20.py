class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # avoid key error
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1 # list: index -> value
            res[tuple(count)].append(s) # list couldn't be key
        return list(res.values())

# time O(m * n) m = lenght of the array; n = average length of string
# space O(m * n)