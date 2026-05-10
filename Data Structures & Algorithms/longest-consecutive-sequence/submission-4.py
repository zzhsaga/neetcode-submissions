class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        visited = set()
        longest_length = 0
        for num in nums_set:
            if num in visited:
                continue
            visited.add(num)
            curr_length = 1
            
            lower = num - 1
            while lower in nums_set:
                visited.add(lower)
                curr_length += 1
                lower -= 1
            higher = num + 1
            while higher in nums_set:
                visited.add(higher)
                curr_length += 1
                higher += 1


            longest_length = max(curr_length, longest_length)
        
        return longest_length
            
        