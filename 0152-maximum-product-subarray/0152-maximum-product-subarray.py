class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        min_prod = nums[0]
        max_prod = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            temp_max = max_prod

            max_prod = max(num, max_prod * num, min_prod * num)
            min_prod = min(num, temp_max * num, min_prod * num)
            result = max(result,max_prod)
        return result

        