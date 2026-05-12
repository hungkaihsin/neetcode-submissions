class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT) # number of ch that meet the requirement
        res, resLen = [-1, -1], float("inf") # start with random (-1, -1) is no meaning
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1 # number of ch that meet the requirement

            while have == need: # shrink the window
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1 # update the shortest window
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""
# time O(m + n) n = length of the string m = unique character
# space O(m)
