class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def search(start,path):
            if start > l - 1:
                return
            path.append(nums[start])
            # print(path)
            if path not in subset:
                subset.append(path[:])
            for nxt in range(start + 1,l):
                search(nxt,path)
            path.pop()


        l = len(nums)

        subset = [[]]

        for i, num in enumerate(nums):
            search(i,[])
        
        return subset