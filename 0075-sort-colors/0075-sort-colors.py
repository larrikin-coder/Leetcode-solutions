class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0]*3
        for num in nums:
            arr[num] += 1
        index = 0
        for color in range(3):
            for _ in range(arr[color]):
                nums[index] = color
                index += 1 

