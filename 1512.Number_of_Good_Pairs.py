class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        temp = 0
        if nums is None or len(nums) == 0:
            return temp
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] == nums[y]:
                    temp += 1
        return temp

