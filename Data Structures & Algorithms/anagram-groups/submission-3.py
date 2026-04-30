class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in tracker:
                tracker[key] = []
            tracker[key].append(word)
        return list(tracker.values()) 
        