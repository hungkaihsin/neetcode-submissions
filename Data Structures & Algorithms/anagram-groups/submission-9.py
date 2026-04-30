class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        key_word = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in key_word:
                key_word[key] = []
            key_word[key].append(word)
        return list(key_word.values())