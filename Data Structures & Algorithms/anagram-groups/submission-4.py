class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_group = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in str_group:
                str_group[key] = []
            str_group[key].append(word)
        return list(str_group.values())