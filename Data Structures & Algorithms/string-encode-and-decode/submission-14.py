class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for s in strs:
            length = len(s)
            encoded_strs += str(length) + "$" + s
        print(encoded_strs)
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        ans = []

        i = 0
        number_str = ''
        while i < len(s):
            
            if s[i] == "$":
                number_count = int(number_str)
                end = i+1+number_count
                ans.append(s[i+1:end])
                i = end
                number_str = ""
            else:
                number_str += s[i]
                i += 1
            
        return ans
