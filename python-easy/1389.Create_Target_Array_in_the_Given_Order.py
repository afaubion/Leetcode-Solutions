class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i, val in enumerate(index):            
            result.insert(val, nums[i])

        return result