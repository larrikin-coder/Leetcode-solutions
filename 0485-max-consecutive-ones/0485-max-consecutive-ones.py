class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #sliding window approach
        max_consecutives = 0
        current_max = 0
        for num in nums:
            if num == 1:
                current_max += 1
                max_consecutives = max(max_consecutives,current_max)
            else:
                current_max = 0
        return max_consecutives


