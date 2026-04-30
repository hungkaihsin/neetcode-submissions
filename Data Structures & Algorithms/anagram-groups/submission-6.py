class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_group = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in word_group:
                word_group[key] = []
            word_group[key].append(word)
        return list(word_group.values())