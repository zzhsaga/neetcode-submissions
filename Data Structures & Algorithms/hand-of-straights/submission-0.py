class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # check if n is valid
        # 
        hand_count = Counter(hand)
        keys = list(hand_count.keys())
        keys.sort()
        
        while hand_count:
            print(hand_count,keys)
            curr = keys[0]
            prev_count = hand_count[curr]
            for _ in range(groupSize):
                if curr not in hand_count or hand_count[curr] < prev_count:
                    return False
                hand_count[curr] -= prev_count
                if hand_count[curr] <= 0:
                    del hand_count[curr]
                    keys.remove(curr)
                curr += 1


        return True
