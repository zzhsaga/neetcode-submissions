class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        arr = []
        for num, cnt in counter.items():
            arr.append([cnt,num])
        arr.sort(reverse = True)
        
        for i in range(k):
            ans.append(arr[i][1])

        return ans