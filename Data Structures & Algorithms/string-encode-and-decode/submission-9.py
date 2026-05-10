class Solution:

    def encode(self, strs: List[str]) -> str:
        # if not strs:
        #     return []
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + '#' + s 
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            rest = int(s[i:j])
            curr = s[j + 1:j+rest + 1]
            ans.append(curr)
            i = j + rest + 1
            print(i)

        # for i in range(len(s)):
        #     if not word:
        #         if s[i] == '#':
        #             rest = int(curr)
        #             word = True
        #             curr = ""
        #         else:
        #             curr += s[i]
        #     else:
        #         curr += s[i]
        #         rest -= 1
        #     if rest == 0:
        #         ans.append(curr)
        #         word = False
        #         curr = ""
        #         rest = len(s)
            
        return ans

        