class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg = [],[]
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        for i in range(len(pos)):
            nums[2*i],nums[2*i+1] = pos[i],neg[i]#2*i puts pos in even place and 2*i+1 put neg in an odd place
        # print(nums)
        return nums
            
        