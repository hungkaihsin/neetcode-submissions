class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str =  ''
        for s in strs:
            encode_str += str(len(s)) + '#' + s
        return encode_str



    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_str = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start_of_str = j + 1
            end_of_str = start_of_str + length
            decoded_str.append(s[start_of_str: end_of_str])
            i = end_of_str
        return decoded_str