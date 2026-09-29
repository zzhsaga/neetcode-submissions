class Solution:
    # ["abc", "ab", ""]
    # abcab
    # abc/ab/
    # ['abc','/ab']
    # abc//ab
    # abc, "", ab
    # 3abc3/ab
    # '2bc'
    # 32bc3/ab
    # 3/2bc3//ab
    # 3 / 2bc
    # 3 / /ab
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + '#' + s

        return encoded_str

    def decode(self, s: str) -> List[str]:

        decoded_list = []

        str_number = "0"

        i = 0

        while i < len(s):
            if s[i] == '#':
                count = int(str_number)
                start = i + 1
                end = i + 1 + count
                decoded_list.append(s[start:end])
                i = end
                str_number = "0"
            else:
                str_number += s[i]
                i += 1
        
        return decoded_list

