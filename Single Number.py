class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counting = 0
        while counting < len(nums):
            if nums.count(nums[counting]) < 2:
                return nums[counting]
            counting += 1