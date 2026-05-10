class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force way is set a window and max() every time
        max_list = []
        l = 0
        for r in range(k,len(nums)+1):
            max_list.append(max(nums[l:r]))
            l += 1
        return max_list


