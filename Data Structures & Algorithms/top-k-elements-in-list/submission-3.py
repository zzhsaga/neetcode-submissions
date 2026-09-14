class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        pairs = []
        for key in counter:
            pairs.append((counter[key],key))
        
        pairs.sort(reverse = True)
        ans = []
        for i in range(k):
            ans.append(pairs[i][1])
        
        return ans

