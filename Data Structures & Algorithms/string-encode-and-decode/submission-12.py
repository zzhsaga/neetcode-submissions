class Solution:

    def encode(self, strs: List[str]) -> str:
        # iterate the strs
        # for each, count the length and encode it as prefix
        # 45# str
        # " "
        # 1# 
        # ""
        # 0#
        # "12#f"
        # 3# 12#f

        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        print(s)
        strs = []
        i = 0
        # read s one by one
        # status length/#/encoded
        length_str = ""
        while i < len(s):
            if s[i] != '#':
                length_str += s[i]
            else:
                length = int(length_str)
                word = s[i+1:i+length+1]
                strs.append(word)
                length_str = ""
                i += length
            i += 1


        return strs

            
