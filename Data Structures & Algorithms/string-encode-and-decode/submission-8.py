class Solution:

    def encode(self, strs: List[str]) -> str:
        # if not strs:
        #     return []
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + '#' + s 
        return encoded_str

    def decode(self, s: str) -> List[str]:
        word = False
        rest = len(s)
        curr_num = ""
        curr = ""
        ans = []

        for i in range(len(s)):
            if not word:
                if s[i] == '#':
                    rest = int(curr_num)
                    word = True
                    curr_num = ""
                else:
                    curr_num += s[i]
            else:
                curr += s[i]
                rest -= 1
            if rest == 0:
                ans.append(curr)
                word = False
                curr = ""
                rest = len(s)
            
        return ans

        