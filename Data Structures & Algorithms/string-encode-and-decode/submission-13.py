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
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j+1+length
            curr = s[j+1: i]
            strs.append(curr)

            


        return strs

            
