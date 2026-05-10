class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def check(s1: str, s2: str) -> bool:
            if len(s1) != len(s2):
                return False
            memo = [0]*26
            base = ord('a')
            for i in range(len(s1)):
                print(s1,i)
                memo[ord(s1[i]) - base] += 1
                memo[ord(s2[i]) - base] -= 1
            
            for count in memo:
                if count != 0:
                    return False
            return True
                
            
        ans = []

        for s in strs:
            exist = False
            for i,v in enumerate(ans):
                curr = v[0]
                if check(s,curr):
                    ans[i].append(s)
                    exist = True
                    break
            if not exist:
                ans.append([s])
        
        return ans

    
            
        