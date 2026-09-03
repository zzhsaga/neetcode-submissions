class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        needed = [0, 0, 0]
        for triplete in triplets:
            valid = []
            for i in range(len(triplete)):
                if triplete[i] > target[i]:
                    valid = []
                    break
                elif triplete[i] == target[i]:
                    valid.append(1)
                else:
                    valid.append(0)
            
            if not valid:
                    continue
                
            for i in range(len(target)):
                needed[i] = max(needed[i],valid[i])
        
        if 0 in needed:
            return False
        else:
            return True
                

            
        