class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # start pointer
        while i < len(s):
            j = i # track "#"
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # number of length
            
            i = j + 1 # start of the string
            j = i + length # end of the string
            res.append(s[i:j])
            i = j # update the pointer
        return res
        
# time O(m) total number of ch
# space O(m + n)
