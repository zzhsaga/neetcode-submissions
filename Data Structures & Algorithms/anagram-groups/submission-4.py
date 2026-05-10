class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def check(s1: str, s2: str) -> bool:
        #     if len(s1) != len(s2):
        #         return False
        #     memo = [0]*26
        #     base = ord('a')
        #     for i in range(len(s1)):
        #         print(s1,i)
        #         memo[ord(s1[i]) - base] += 1
        #         memo[ord(s2[i]) - base] -= 1
            
        #     for count in memo:
        #         if count != 0:
        #             return False
        #     return True
                
            
        check_dict = {}

        for s in strs:
            seri_s = ''.join(sorted(s))
            if seri_s in check_dict:
                check_dict[seri_s].append(s)
            else:
                check_dict[seri_s] = [s]
        
        return list(check_dict.values())

    
            
        