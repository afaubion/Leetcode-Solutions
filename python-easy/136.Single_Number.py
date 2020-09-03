class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        duplicates = {}
        for char in nums:
        ## checking whether the char is already present in dictionary or not
            if char in duplicates:
        ## increasing count if present
                duplicates[char] += 1
            else:
            ## initializing count to 1 if not present
                duplicates[char] = 1
        for key, value in duplicates.items():
            if value == 1:
                return key