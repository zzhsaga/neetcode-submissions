class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter e.g. [freq, num]
        # sort the counter, min to max
        counter = Counter()
        for num in nums:
            counter[num] += 1
        
        freq_num_list = []
        for num in counter:
            freq = counter[num]
            freq_num_list.append([freq, num])

        freq_num_list.sort()

        ans = []

        for i in range(k):
            num = freq_num_list[-i-1][1]
            ans.append(num)

        return ans
        
